# Document To Read Before Coding

This document will focus on how to get involved into Flink development and how to contribute code. It is written for experienced developers proficient with Flink concepts and architecture, e.g. stateful distributed stream processing, Flink runtime component, layered APIs, etc. Flink provides the [Hands-On Training](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/learn-flink/overview/) for this.

## Big Picture

[The Flink roadmap](https://flink.apache.org/roadmap.html), especially the Feature Radar section, is the great info source to understand the big picture. The Feature Stages show us the most interesting components and their development status:

> ### Feature Stages <a id="feature-stages"></a>
>
> * **MVP:** Have a look, consider whether this can help you in the future.
> * **Beta:** You can benefit from this, but you should carefully evaluate the feature.
> * **Ready and Evolving:** Ready to use in production, but be aware you may need to make some adjustments to your application and setup in the future, when you upgrade Flink.
> * **Stable:** Unrestricted use in production
> * **Reaching End-of-Life:** Stable, still feel free to use, but think about alternatives. Not a good match for new long-lived projects.
> * **Deprecated:** Start looking for alternatives now

![](../.gitbook/assets/image%20%281%29.png)

{% hint style="warning" %}
Put your focus on the Beta, Ready&Evolving, MVP stages. Avoid spending time on phasing out features.
{% endhint %}

It is highly recommended to ready whole page of the roadmap. The content is very valuable. After doing that, you can glance over [Community & Project Info](https://flink.apache.org/community.html) to get information about the mailing lists, Jira issue tracker, project wiki, contact to committers, etc. for the daily development. 



