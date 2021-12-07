---
description: >-
  A real case study of how to setup the logs to get insight information of how
  SQL query works in ITCase environment by using TableEnvironment based on
  HBaseConnectorITCase
---

# Solving issues in ITCase

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

With this setup, all INFO level log messages of hbase2 connector and minicluster and only WARN level log messages of other components will be shown in the rolling files.&#x20;

In case you want to see the log in the console, you can activate the STDOUT appenderRef.

{% hint style="info" %}
It is recommend the set **rootLogger.level = INFO** for your first check of an ITCa**se**
{% endhint %}

## Find the root cause of issue [FLINK-24077](https://issues.apache.org/jira/browse/FLINK-24077)

Make sure you have built Flink. Now go to the Flink root directory and run:

```
mvn test 
-Dtest=HBaseConnectorITCase 
-Dinclude_hadoop_aws 
-Dhadoop.version=2.8.3 
-pl flink-connectors/flink-connector-hbase-2.2
```











## MiniCluster has impact on TableEnvironment













## Control the lifecycle of the MiniCluster





















## Write the ITCase efficiently



