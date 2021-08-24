# 101 - Getting started with Flink Development

Flink provides very comprehensive document you need to develop Flink or use Flink to develop your application. This document will try to point out the most important steps and hint to get the environment ready.

Flink 1.13 is used for this guide. 

## Get the code and build Flink

{% hint style="warning" %}
To save your time, Java 11, Intellij Idea, and maven 3.2.5 are recommended
{% endhint %}

Fork your own Flink repo and checkout source code from Github and run:

```
$ mvn clean install -DskipTests
```

If you are behind firewall, e.g. working in China, and have issue to access some dependencies, you might consider to use mirror in your maven settings.xml:

```markup
    <mirror>
      <id>nexus-aliyun</id>
      <name>Nexus aliyun</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </mirror>
```

You can read the official doc from Flink for further information in details:

[**https://cwiki.apache.org/confluence/display/FLINK/Setting+up+a+Flink+development+environment**](https://cwiki.apache.org/confluence/display/FLINK/Setting+up+a+Flink+development+environment)

[**https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/flinkdev/building/**](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/flinkdev/building/)\*\*\*\*

## Setup Intellij Idea

Open Flink as a project is easy but the IDE setup of Intellij Idea will take about one hour for the first time**:** [**https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/flinkdev/ide\_setup/**](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/flinkdev/ide_setup/)

{% hint style="info" %}
The setup of code formatting and Save Actions are important. It will avoid messing the code up. 
{% endhint %}

{% hint style="danger" %}
you will get stuck at: 8. Build the Project in Intellij Idea \(“Build” → “Build Project”\) because of java 11 issue if only java 8 is installed on your computer. Please read the FAQ, set the project SDK and module SDK to java 8, uncheck the java11 java profile and reload all maven projects.

**To save your time, alternatively, you can just install java 11 before you start clone the repo.**
{% endhint %}

  
****

