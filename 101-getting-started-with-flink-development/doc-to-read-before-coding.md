# Document To Read Before Coding

This document will focus on how to get involved into Flink development and how to contribute code. It is written for experienced developers proficient with Flink concepts and architecture, e.g. stateful distributed stream processing, Flink runtime component, layered APIs, etc. For the developers who are not familiar with these, Flink provides the [Hands-On Training\(One of the best tutorials in the industry\)](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/learn-flink/overview/).

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
Put your focus on the Beta, Ready&Evolving, MVP stages and avoid spending time on phasing out features that will be deprecated in the future.
{% endhint %}

It is highly recommended to ready whole page of the roadmap. The content is very valuable. After doing that, you can glance over [Community & Project Info](https://flink.apache.org/community.html) to get information about the mailing lists, Jira issue tracker, project wiki, contact to committers, etc. for the daily development. 

## Contribution Matters Needing Attention

All important information about the contribution is described in [How To Contribute](https://flink.apache.org/contributing/how-to-contribute.html) and the sections underneath. You can contribute code, document, and websites. The process described there is very precise and detailed. It has some common parts, like you have to follow the [code style and code formatting, fulfill the code quality requirement](https://flink.apache.org/contributing/code-style-and-quality-preamble.html); you should understand the [PR review process](https://flink.apache.org/contributing/reviewing-prs.html) very well to make sure your PR contains the right information so that it will be review and accepted. Beyond these common parts, there are some special matters that need attention:

* Consensus is the king. Use mailing list to trigger discussion and reach the consensus. Big design concept can described with a [FLIP](https://cwiki.apache.org/confluence/display/FLINK/Flink+Improvement+Proposals). Use Jira to summarize the result and break down the tasks. And, obviously, use Github for the PR review and merge.
* Document contribution requires both [English and Chinese](https://flink.apache.org/contributing/contribute-documentation.html).

{% hint style="warning" %}
Get consensus with the committer, before you try to contribute code.
{% endhint %}



