# openAI API use:
- [openAI API use:](#openai-api-use)
  - [Key concepts(关键概念):](#key-concepts关键概念)
    - [Text generation models(文本生成模型):](#text-generation-models文本生成模型)
    - [Assistant:](#assistant)
    - [Embeddings(词嵌入):](#embeddings词嵌入)
    - [Tokens:](#tokens)
  - [Developer quickstart(开发者快速入门):](#developer-quickstart开发者快速入门)
    - [Get up and running with the OpenAI API(快速开始使用OpenAI API):](#get-up-and-running-with-the-openai-api快速开始使用openai-api)
    - [Account setup(账户设置):](#account-setup账户设置)
    - [API Keys:](#api-keys)

"Head to chat.openai.com."：这部分是一个建议或指令，意思是“前往 chat.openai.com。”。“Head to”是一个常用的英语短语，用来建议某人去某个地方。在这里，它意味着如果你想使用或了解更多关于ChatGPT的信息，应该访问网址“chat.openai.com”，这是一个特定的网站链接。<br>

Explore the API(探索这个应用程序编程接口 (API))<br>

[Watch the first OpenAI Developer Day keynote(观看首届 OpenAI 开发者日主题演讲)](https://youtu.be/U9mJuUkhUzk)

> OpenAI Developer Day:指的是由 OpenAI 组织的一个开发者日活动。
> keynote: 这个词在这里指的是某个会议或活动中的主要演讲或主题演讲。通常，这种演讲由重要人物进行，旨在阐述会议的主要主题或传达重要信息。

The OpenAI API can be applied to virtually any task. We offer a range of models with different capabilities and price points, as well as the ability to fine-tune custom models.

OpenAI API 实际上可以应用于任何任务。我们提供一系列具有不同功能和价格点的模型，以及微调定制模型的能力。


🚨🚨🚨Note:<br>

----

你可以在使用 openAI API 的过程中见到以下图片:

![](./materials/uasge_limit.jpg)

这是提醒你:

您已达到使用限额。欲了解更多详情，请查看您的使用仪表板和账单设置。如果您还有其他问题，请通过我们的帮助中心 help.openai.com 与我们联系。

----


## Key concepts(关键概念):

### Text generation models(文本生成模型):

OpenAI's text generation models (often referred to as generative pre-trained transformers or "GPT" models for short), like GPT-4 and GPT-3.5, have been trained to understand natural and formal(正式的) language. Models like GPT-4 allows text outputs in response to their inputs. **The inputs to these models are also referred to as "prompts".** Designing a prompt is essentially(本质上) how you "program" a model like GPT-4, usually by providing instructions(指令) or some examples of how to successfully complete a task. Models like GPT-4 can be used across a great variety of tasks including content or code generation, summarization, conversation, creative writing(创意写作), and more. Read more in our introductory text generation guide and in our prompt engineering guide.<br>

OpenAI的文本生成模型（通常被称为生成式预训练transformers，简称“GPT”模型），比如GPT-4和GPT-3.5，已被训练以理解自然语言和正式语言。像GPT-4这样的模型可以根据输入生成文本输出。**这些模型的输入也被称为“提示”**。设计一个提示本质上就是如何“编程”一个像GPT-4这样的模型，通常是通过提供指令或一些示例来展示如何成功完成一个任务。像GPT-4这样的模型可以应用于广泛的任务，包括内容或代码生成、摘要、对话、创意写作等等。欲了解更多，请阅读我们的入门文本生成指南和提示工程指南。<br>

### Assistant:

Assistants refer to entities, which in the case of the OpenAI API are powered by large language models like GPT-4, that are capable of performing(执行) tasks for users. These assistants operate based on the instructions(指令) embedded within the context window of the model. They also usually have access to tools which allows the assistants to perform more complex tasks like running code or retrieving(检索) information from a file. Read more about assistants in our Assistants API Overview.<br>

Assistants是指由大型语言模型（如 GPT-4）驱动的实体，在 OpenAI API 的情况下，这些Assistants能够为用户执行任务。这些Assistants的运作基于嵌入在模型的上下文窗口中的指令。它们通常还可以访问工具，使Assistants能夠执行更复杂的任务，如运行代码或从文件中检索信息。欲了解更多关于Assistants的信息，请阅读我们的Assistants API 概览。<br>

### Embeddings(词嵌入):

An embedding is a vector representation(表示) of a piece of data (e.g. some text) that is meant to preserve(保留) aspects(方面) of its content and/or its meaning. Chunks of data(数据块) that are similar in some way will tend(趋向) to have embeddings that are closer together than unrelated data. OpenAI offers text embedding models that take as input a text string and produce as output an embedding vector. Embeddings are useful for search, clustering, recommendations, anomaly(异常) detection, classification, and more. Read more about embeddings in our embeddings guide.<br>

Embedding是一种数据（例如某些文本）的向量表示形式，旨在保留其内容和/或含义的某些方面。在某种程度上相似的数据块，其embedding通常会比不相关数据的embedding更为接近。OpenAI提供了文本embedding模型，这些模型以文本字符串作为输入，并产生embedding向量作为输出。Embedding对于搜索、聚类、推荐、异常检测、分类等领域非常有用。想了解更多关于embedding的信息，请阅读我们的embedding指南。<br>

### Tokens:

Text generation and embeddings models process text in chunks called tokens. Tokens represent commonly occurring sequences of characters. For example, the string " tokenization" is decomposed(分解) as " token" and "ization", while a short and common word like " the" is represented as a single token. **Note that in a sentence, the first token of each word typically starts with a space character.** Check out our tokenizer tool(分词工具) to test specific strings and see how they are translated into tokens. As a rough rule of thumb, 1 token is approximately(大概) 4 characters(字符) or 0.75 words for English text.<br>

> "thumb" 在英语中的字面意思是“拇指”。但在这个上下文中，"rule of thumb" 是一个成语，意思是“经验法则”或“粗略的估计方法”。

文本生成和Embeddings模型通过被称为 tokens 的单元来处理文本。Tokens 代表常见的字符序列。例如，字符串 " tokenization" 被拆分为 " token" 和 "ization"，而像 " the" 这样短小且常见的单词则被表示为一个单独的 token。**请注意，在一个句子中，每个单词的第一个 token 🤨**您可以查看我们的分词工具，测试特定字符串，并查看它们是如何被转换为 tokens 的。作为一个粗略的经验法则，对于英文文本来说，1个 token 大约相当于4个字符或0.75个单词。<br>


## Developer quickstart(开发者快速入门):

### Get up and running with the OpenAI API(快速开始使用OpenAI API):

> “Get up and running” 是一个常用的英语短语，意思是迅速开始或迅速投入到某事中。字面上，“get up”意味着起身或起立，但在这里它更多地表达的是开始行动或启动的意思。

The OpenAI API provides a simple interface for developers(开发者) to create an intelligence layer(智能层) in their applications, powered by OpenAI's **state of the art(最先进的)** models. The Chat Completions(完成) endpoint powers ChatGPT and provides a simple way to take text as input and use a model like GPT-4 to generate an output.<br>

OpenAI的API为开发者提供了一个简单的接口，用于在他们的应用程序中创建一个由OpenAI最先进的模型驱动的智能层。Chat Completions端点驱动了ChatGPT，并提供了一种简单的方式，即接受文本输入，并使用像GPT-4这样的模型来生成输出。<br>

This quickstart is designed to help get your local development environment setup(设置；搭建) and send your first API request(请求). If you are an experienced(经验丰富的) developer or want to just dive into("深入研究";"迅速投入") using the OpenAI API, the API reference of GPT guide are a great place to start. Throughout this quickstart, you will learn:<br>

这份快速入门旨在帮助您搭建本地开发环境并发送您的首个API请求。如果您是一位经验丰富的开发者，或者想直接深入使用OpenAI API，那么**GPT指南中的API参考文档**是一个绝佳的起点。在这份快速入门中，您将学习：<br>

- How to setup your development environment(如何搭建您的开发环境)
- How to install the latest SDKs(如何安装最新的SDK)
- Some of the basic concepts of the OpenAI API(OpenAI API的一些基本概念)
- How to send your first API request(如何发送您的首个API请求)

If you run into any challenges or have questions getting started, please join our developer forum(论坛).<br>

如果在开始过程中遇到任何挑战或有问题，请加入我们的开发者论坛。<br>

### Account setup(账户设置):

First, create an OpenAI account or sign in. Next, navigate(前往；导航至) to the [API key page](https://platform.openai.com/api-keys) and "Create new secret key", optionally(可选) naming the key. Make sure to save this somewhere safe and do not share it with anyone.<br>

首先，创建一个OpenAI账户或登录。接着，前往❤️**API密钥页面**并“创建新的密钥”，可以选择为密钥命名。确保将其保存在安全的地方，并且不要与任何人分享。<br>

### API Keys:

Your secret API keys are listed below. Please note that we do not display your secret API keys again after you generate them.<br>

您的 `secret API keys` 如下所列。请注意，一旦您生成这些密钥，我们将不会再次显示它们。

Do not share your API key with others, or expose it in the browser or other client-side code. In order to protect the security of your account, OpenAI may also automatically disable any API key that we've found has leaked publicly.

Enable tracking to see usage per API key on the Usage page.


| NAME                  | SECRET KEY | TRACKING | CREATED     | LAST USED  |
|-----------------------|------------|----------|-------------|------------|
| peilongchencc_openai  | sk-...eZeu | Enable   | 2023年6月8日 | 2023年6月8日 |

> “TRACKING”列中的“Enable”意思是“启用”。在这里，它表示对该 API 密钥的使用情况进行追踪功能是开启的。这意味着你可以在“使用情况”页面查看到这个特定 API 密钥的使用详情，比如调用次数、使用频率等信息。这个功能对于监控和分析 API 密钥的使用情况非常有用，特别是当你想确保密钥没有被滥用时。

Default organization

If you belong to multiple organizations, this setting controls which organization is used by default when making requests with the API keys above.

Note: You can also specify which organization to use for each API request. See Authentication to learn more.



请不要与他人共享您的 API 密钥，也不要在浏览器或其他客户端代码中暴露它。为了保护您账户的安全，一旦发现有 API 密钥被公开泄露，OpenAI 可能会自动禁用该密钥。

在“使用情况”页面上启用追踪功能，以查看每个 API 密钥的使用情况。

| 名称                  | 秘密密钥    | 追踪功能  | 创建日期     | 最后使用日期  |
|-----------------------|------------|----------|-------------|-------------|
| peilongchencc_openai  | sk-...eZeu | 启用      | 2023年6月8日 | 2023年6月8日 |


默认组织

如果您属于多个组织，此设置将控制在使用上述 API 密钥进行请求时默认使用哪个组织。

备注：您也可以为每个 API 请求指定使用哪个组织。请参阅“身份验证”了解更多信息。


请将下列内容翻译为地道的中文:



"TRACKING"为"Enable"是什么意思？可用？

请将下列内容翻译为地道的英文:

请将图片中的内容转为markdown表格形式