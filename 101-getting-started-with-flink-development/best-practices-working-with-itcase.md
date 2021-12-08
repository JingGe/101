---
description: >-
  A real case study of how to setup the logs to get insight information of how
  SQL query works in ITCase environment by using TableEnvironment based on
  HBaseConnectorITCase
---

# Best Practices working with ITCase

{% hint style="info" %}
GitHub repo: [https://github.com/JingGe/101](https://github.com/JingGe/101)
{% endhint %}

While solving issue in ITCase, the first thing to do is to understand the running process. You can [debug the ITCase](debug-flink-itcase.md) to get runtime information in details. If you want to quickly have a big picture of it, a good choice is to change the log setup to the insight information of the running process.

{% hint style="info" %}
**After reading this section, you will learn:**

1. **how to change the log setup to get required information.**
2. **how to find the root cause of a real issue of HBaseConnectorITCase**
3. **how does the MiniCluster have the impact on TableEnvironment**
4. **how to control the lifecycle of the MiniCluster for ITCase**
5. **how to write an ITCase efficiently**
{% endhint %}

## Change the log setup

Tests in Flink will use log4j2-test.properties under test/resources.&#x20;

By default, the root logger level is set to be OFF.

```
# Set root logger level to OFF to not flood build logs
# set manually to INFO for debugging purposes
rootLogger.level = OFF
```

Since it will take some effort to get the right setup, I have prepared one shows below. You can take it as the staring point for your own purpose.

```
# set to INFO, if you want to know more details about the whole process 
# with the external service, e.g. in this case the HBase 
rootLogger.level = WARN
rootLogger.appenderRef.rolling.ref = RollingFile
# active it if you want to see the log in the console
# rootLogger.appenderRef.stdout.ref=STDOUT

appenders=console, rolling

appender.console.type = Console
appender.console.name = STDOUT
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = %-4r [%t] %-5p %c %x - %m%n

appender.rolling.type = RollingFile
appender.rolling.name = RollingFile
appender.rolling.fileName = target/rolling/rollingtest.log
appender.rolling.filePattern = target/rolling2/test-%d{MM-dd-yy-HH-mm-ss}-%i.log.gz
appender.rolling.layout.type = PatternLayout
appender.rolling.layout.pattern = %d %p %C{1.} %-4r [%t] %x %m%n
appender.rolling.policies.type = Policies
appender.rolling.policies.time.type = TimeBasedTriggeringPolicy
appender.rolling.policies.time.interval = 200
appender.rolling.policies.time.modulate = true
appender.rolling.policies.size.type = SizeBasedTriggeringPolicy
appender.rolling.policies.size.size=100MB

# logger for hbase2 connector
logger.hbase2.name = org.apache.flink.connector.hbase2
logger.hbase2.level = INFO

# logger for minicluster
logger.minicluster.name = org.apache.flink.runtime.minicluster
logger.minicluster.level = INFO
```

With this setup, to minimise the log output, all INFO level log messages of hbase2 connector and minicluster and only WARN level log messages of other components will be shown in the rolling files.&#x20;

In case you want to see the log in the console, you can activate the STDOUT appenderRef.

{% hint style="info" %}
It is recommend the set **rootLogger.level = INFO** for your first check of an ITCa**se**
{% endhint %}

## Find the root cause of issue [FLINK-24077](https://issues.apache.org/jira/browse/FLINK-24077)

{% hint style="info" %}
**It is recommended to set rootLogger.level = INFO for trouble shooting.**
{% endhint %}

Make sure you have built Flink. Now go to the Flink root directory and run:

```
mvn test 
-Dtest=HBaseConnectorITCase 
-Dinclude_hadoop_aws 
-Dhadoop.version=2.8.3 
-pl flink-connectors/flink-connector-hbase-2.2
```

![](<../.gitbook/assets/image (12).png>)

you will see the log has been created:

![](<../.gitbook/assets/image (9).png>)

In the log file you will get details information like a HBase MiniCluster and multiple Flink MiniClusters  will be initialised, how tasks were executed, etc.

When you walk through the log, you will find there are some thrown runtime exception java.lang.IllegalStateException tells us that the MiniCluster is not yet running or has already been shut down, which turns out that the CollectResultFetcher was Failed and some data might be lost.

![](<../.gitbook/assets/image (10).png>)

The root cause is, since the shutdown of the MiniCluster will be called asynchronously, CollectResultFetcher will got data lost sometimes based on race conditions and the unchecked RuntimeException java.lang.IllegalStateException will be thrown that we were not aware of.

{% hint style="danger" %}
Please pay attention that the mavn test was successful even if unchecked exceptions have been thrown.&#x20;
{% endhint %}

## MiniCluster has impact on TableEnvironment for ITCase

Thanks for the details log information, it is easy to be aware that there were multiple Flink MiniClusters that have been started and stopped. Each up and down of a MiniCluster will take about 4s.&#x20;

While we are using TableEnvironment like:

```
StreamExecutionEnvironment execEnv = StreamExecutionEnvironment.getExecutionEnvironment();
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(execEnv, streamSettings);
```

each time when we execute a sql query like:&#x20;

```
tableEnv.sqlQuery("...");
```

a new MiniCluster will be started and then stopped asynchronously after the job is finished in the background.

{% hint style="danger" %}
By default, running each query via TableEnvironment in ITCase will trigger a new MiniCluster being started and stopped in the background. It will cost time and resource.
{% endhint %}

## Control the lifecycle of the MiniCluster

The idea case is to control the lifecycle of the MiniCluster manually for each ITCase. While we execute sql via TableEnvironment, it will check whether a MiniCluster is available. If yes, the available MiniCluster will be used for job submission.

In this case, you can use JUnit @ClassRule and @Rule and the MiniClusterWithClientResource provided by Flink:

```
@ClassRule
public static final MiniClusterWithClientResource MINI_CLUSTER = 
       new MiniClusterWithClientResource(                
              new MiniClusterResourceConfiguration.Builder()                        
                     .setConfiguration(new Configuration())                        
                     .build());
```

Using @ClassRule will make sure a MiniCluster will be initialised before any test methods are running and stopped after all test methods are finished. In this way, the race conditions mentioned previously are solved.

## Write the ITCase efficiently

By default, each query will trigger a new MiniCluster up and down. you can image how much time and resource it will cost when we run hundreds even thousands of queries.&#x20;

After using @ClassRule to control it, the maven takes 1:38 min:

![](<../.gitbook/assets/image (11).png>)

Don't under estimate the improvement. After considering the time cost of HBase initialisation, job submit and execution etc., each test method may only cost few seconds to finish. Compare to the last maven test, we saved 15 seconds for 9 tests. The performance improvement is significantly.

{% hint style="warning" %}
Please be aware that most of ITCases are working with MiniCluster implicitly or explicitly.
{% endhint %}

{% hint style="info" %}
**It is generally recommended to control external resource like MiniCluster at the class level for ITCase unless there is a technical reason for using extra individual MiniClusters for some test methods.**
{% endhint %}
