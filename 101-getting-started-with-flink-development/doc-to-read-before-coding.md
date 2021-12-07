# Document To Read Before Coding

This document will focus on how to get involved into Flink development and how to contribute code. It is written for experienced developers proficient with Flink concepts and architecture, e.g. stateful distributed stream processing, Flink runtime component, layered APIs, etc. For the developers who are not familiar with these, Flink provides the [Hands-On Training(One of the best tutorials in the industry)](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/learn-flink/overview/).

## Big Picture

[The Flink roadmap](https://flink.apache.org/roadmap.html), especially the Feature Radar section, is the great info source to understand the big picture. The Feature Stages show us the most interesting components and their development status:

> ### Feature Stages <a href="#feature-stages" id="feature-stages"></a>
>
> * **MVP:** Have a look, consider whether this can help you in the future.
> * **Beta:** You can benefit from this, but you should carefully evaluate the feature.
> * **Ready and Evolving:** Ready to use in production, but be aware you may need to make some adjustments to your application and setup in the future, when you upgrade Flink.
> * **Stable:** Unrestricted use in production
> * **Reaching End-of-Life:** Stable, still feel free to use, but think about alternatives. Not a good match for new long-lived projects.
> * **Deprecated:** Start looking for alternatives now

![](<../.gitbook/assets/image (1).png>)

{% hint style="warning" %}
Put your focus on the Beta, Ready\&Evolving, MVP stages and avoid spending time on phasing out features that will be deprecated in the future.
{% endhint %}

It is highly recommended to ready whole page of the roadmap. The content is very valuable. After doing that, you can glance over [Community & Project Info](https://flink.apache.org/community.html) to get information about the mailing lists, Jira issue tracker, project wiki, contact to committers, etc. for the daily development.&#x20;

## Contribution Matters Needing Attention

All important information about the contribution is described in [How To Contribute](https://flink.apache.org/contributing/how-to-contribute.html) and the sections underneath. You can contribute code, document, and websites. The process described there is very precise and detailed. It has some common parts, like you have to follow the [code style and code formatting, fulfill the code quality requirement](https://flink.apache.org/contributing/code-style-and-quality-preamble.html); you should understand the [PR review process](https://flink.apache.org/contributing/reviewing-prs.html) very well to make sure your PR contains the right information so that it will be reviewed and accepted; etc.&#x20;

{% hint style="info" %}
This document only shows you some most important rules. You will not make big mistake if you start contribute code only based on this document. But, It is highly recommended that you should read all information under [How To Contribute](https://flink.apache.org/contributing/how-to-contribute.html).&#x20;
{% endhint %}

Beyond these common parts, there are some special matters that need attention:

* Consensus is the king. Use mailing list to trigger discussion and reach the consensus. Big design concept can described with a [FLIP](https://cwiki.apache.org/confluence/display/FLINK/Flink+Improvement+Proposals). Use Jira to summarize the result and break down the tasks. And, obviously, use Github for the PR review and merge.
* Document contribution requires both [English and Chinese](https://flink.apache.org/contributing/contribute-documentation.html).
* There is a template for you to create new PR.
* [Separation Of Concern](https://flink.apache.org/contributing/code-style-and-quality-pull-requests.html): Pull Requests must put cleanup, refactoring, and core changes into separate commits. These commits should be described in the **Brief change log** section of the PR. You can find an excellent example in [https://github.com/apache/flink/pull/7264](https://github.com/apache/flink/pull/7264).&#x20;
* [Flink has naming scheme for commits](https://cwiki.apache.org/confluence/display/FLINK/Apache+Flink+development+guidelines). The basic naming scheme for commits is \[Jira issue|hotfix] \[component] Message. Multiple commits may refer to the same issue, if the issue is fixed in multiple steps.
* Flink has its [own annotations](https://cwiki.apache.org/confluence/display/FLINK/Stability+Annotations) you should pay attention to while reading/contributing code.
* Flink emphasized how important it is to have high quality and well engineered code. I personally strongly recommend the [Clean Code concept from Uncle Bob](https://www.goodreads.com/book/show/3735293-clean-code). Furthermore, there are some professional softwares, e.g. [SonarGraph](https://www.hello2morrow.com/products/sonargraph), take care of even deeper issues about the code and software architecture.
* There are [trade-offs](https://flink.apache.org/contributing/code-style-and-quality-common.html) to write code for data intensive processing, while code for coordination should continue keeping simple and clean, again Clean Code.
* Flink keeps the dependency footprint small to avoid dependency clashes, e.g. extra framework like Guice will not be used for dependency injection purpose.
* [Avoid Mockito](https://docs.google.com/presentation/d/1fZlTjOJscwmzYadPGl23aui6zopl94Mn5smG-rB0qT8/edit#slide=id.g2fa61f7d00\_0\_136) - Use reusable test implementations

{% hint style="danger" %}
**Get consensus with the committer, before you try to contribute code.**
{% endhint %}

{% hint style="danger" %}
**Well engineered code is a must.**
{% endhint %}

{% hint style="info" %}
Flink PR has a template with the following sections:

* **What is the purpose of the change**
* **Open Architecture Questions (optional)**
* **Further ToDos and Follow-ups (optional)**
* **Brief change log**
* **Verifying this change**
* **Does this pull request potentially affect one of the following parts:**
* **Documentation**
{% endhint %}

{% hint style="info" %}
Naming scheme for commits \[Jira issue|hotfix] \[component] Message, e.g.:



```
[FLINK-1234] [runtime] Runtime support some cool new thing
[FLINK-1234] [java api] Add hook for cool thing to java api
[FLINK-1234] [scala api] Add hook for that thing to scala api
[FLINK-1234] [optimizer] Make optimizer aware that it can exploit this thing

[hotfix] [docs] Extend state checkpointing protocol
```
{% endhint %}

