# Setup Flink Development Environment

Flink provides very comprehensive document you might need to develop Flink or to use Flink to develop your own application. This document will focus on pointing out the most important steps and hint to get the environment ready. The goal is clear: save your time as more as possible.

This document is valid for Flink 1.13. It took me more than two days to get everything done. Hope the estimated time could be optimized to less than 3 hours, if you follow this guide. 

## Get the code and build Flink

{% hint style="warning" %}
**To save your time, Java 11, Intellij Idea, and maven 3.2.5 are recommended**
{% endhint %}

Make sure you have Java 11 and Maven 3.2.5 installed. Fork your own Flink repo and checkout the source code from Github and run:

```
$ mvn clean install -DskipTests
```

If you are behind firewall, e.g. working in China, and have issue to access some dependencies, you might consider using mirror in your maven settings.xml, for example in China:

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
The setup of code formatting and Save Actions are important. It will avoid messing the code up. Worth doing it!
{% endhint %}

{% hint style="danger" %}
I had got stuck at: 8. Build the Project in Intellij Idea \(“Build” → “Build Project”\) for java 11 issue because only java 8 was installed on my computer. It took me hours to fix it. After searching and reading a lot of docs and blogs, finally found the right info at [FAQ section](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/flinkdev/ide_setup/). Problem solved after setting the project SDK and module SDK to java 8, unchecking the java11 maven profile and reloading all maven projects.

**Alternatively, just install java 11 before you start cloning the repo. This will save you a lot of time.**
{% endhint %}

Now you should have a clean Flink development env ready on your local computer.   
****

