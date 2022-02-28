---
description: Using HBaseConnectorITCase as the real case
---

# Debug Flink ITCase

{% hint style="info" %}
GitHub repo: [https://github.com/JingGe/101](https://github.com/JingGe/101)
{% endhint %}

Most of the Flink ITCase can be run as same as the normal unit test, you can therefore debug it in the IntelliJ IDEA. For some complicated ITCase, if it could not run in the IDEA, you can consider setting up the remote debugging.

In this section we will use the real ITCase HBaseConnectorITCase as the example, so you can use it in your daily development.

There 3 steps to get the remote debugging done:

## 1. Run ITCase with maven command line

Go to the root directory of Flink project and run:

> <mark style="color:blue;">**\<your\_dir>/flink/mvn test -Dtest=HBaseConnectorITCase -Dinclude\_hadoop\_aws -Dhadoop.version=2.8.3 -Dmaven.surefire.debug -pl flink-connectors/flink-connector-hbase-2.2**</mark>

Alternatively, you can also to the Flink sub module directory, flink-connector-hbase-2.2 in this case, and run:

> <mark style="color:blue;">**\<your\_dir>/flink/flink-connectors/flink-connector-hbase-2.2(FLINK-24753✔) ➭ mvn test -Dtest=HBaseConnectorITCase -Dinclude\_hadoop\_aws -Dhadoop.version=2.8.3 -Dmaven.surefire.debug**</mark>

you will see in the command line output:

> **Listening for transport dt\_socket at address: 5005**

Step 1 is done, let's move to step 2.

## 2. Set up remote debugging in IDEA

If you are not familiar with the remote debug setup in IntelliJ IDEA, please refer to [https://www.jetbrains.com/help/idea/tutorial-remote-debug.html#be0ec68f](https://www.jetbrains.com/help/idea/tutorial-remote-debug.html#be0ec68f)

For this case, the setup will look like this:

![](<../.gitbook/assets/image (13) (1).png>)

Step 2 is done, let's move to step 3.

## 3. Set up break points and Start the debug

Now you can set up some break points in your class and start debug in the IDEA. You will see that the process in the command line will be moving forward:

> Listening for transport dt\_socket at address: 5005 Running&#x20;
>
> **org.apache.flink.connector.hbase2.HBaseConnectorITCase**&#x20;
>
> **Formatting using clusterid: testClusterID**

And in the IDEA, you will see the the process is paused at the break point, like this:

![](<../.gitbook/assets/image (10).png>)

Now happy debugging!

