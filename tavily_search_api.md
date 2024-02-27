# Tavily

Tavily是为 **大型语言模型**（LLMs）和 **生成式检索增强**（RAG, Retrieval-Augmented Generation）优化的搜索引擎，旨在提供高效、快速且持久的搜索结果。<br>

与其他搜索API（如Serp或Google）不同，Tavily专注于为AI开发人员和自主AI代理优化搜索，承担搜索、抓取、过滤和提取在线源中最相关信息的所有负担，所有这些都通过单一API调用完成。此外，Tavily还利用专有的金融、代码、新闻等内部数据源来补充在线信息。<br>

- [Tavily](#tavily)
  - [获取"TAVILY\_API\_KEY":](#获取tavily_api_key)
  - [Tavily Search API](#tavily-search-api)
    - [github实例--GPT Researcher:](#github实例--gpt-researcher)
  - [关于 Tavily 的常见问题:](#关于-tavily-的常见问题)
    - [How is Tavily Search API different from other APIs(Tavily 搜索 API 与其他 API 有何不同)?](#how-is-tavily-search-api-different-from-other-apistavily-搜索-api-与其他-api-有何不同)
    - [What kind of research does Tavily conduct(执行；进行；实施)(Tavily 进行什么类型的搜索)?](#what-kind-of-research-does-tavily-conduct执行进行实施tavily-进行什么类型的搜索)
    - [How does Tavily ensure the accuracy of the information provided(Tavily 如何确保所提供信息的准确性)?](#how-does-tavily-ensure-the-accuracy-of-the-information-providedtavily-如何确保所提供信息的准确性)
    - [How can I integrate with Tavily Search API(我如何与 Tavily 搜索 API 进行集成)?](#how-can-i-integrate-with-tavily-search-api我如何与-tavily-搜索-api-进行集成)
    - [Can I test Tavily API before purchasing(在购买之前我可以测试 Tavily API 吗)?](#can-i-test-tavily-api-before-purchasing在购买之前我可以测试-tavily-api-吗)
    - [Does Tavily include sources in the research results(Tavily 的搜索结果中是否包含来源信息)?](#does-tavily-include-sources-in-the-research-resultstavily-的搜索结果中是否包含来源信息)
    - [Is Tavily suitable for individual or enterprise(大型的商业组织或公司) needs(Tavily 适合个人还是企业需求)?](#is-tavily-suitable-for-individual-or-enterprise大型的商业组织或公司-needstavily-适合个人还是企业需求)
    - [What is the Tavily Partners program(Tavily 合作伙伴计划是什么)?](#what-is-the-tavily-partners-programtavily-合作伙伴计划是什么)
  - [学习LangChain中的Agent，LangChain官方使用的是 Tavily Search API ，个人能够使用 google search api 吗？](#学习langchain中的agentlangchain官方使用的是-tavily-search-api-个人能够使用-google-search-api-吗)
  - [Tavily Python SDK:](#tavily-python-sdk)
    - [安装方式:](#安装方式)
    - [使用:](#使用)
    - [API Methods(API 方法) 📚:](#api-methodsapi-方法-)
      - [Client(客户端):](#client客户端)
      - [Methods:](#methods)
      - [Keyword Arguments 🖊️:](#keyword-arguments-️)
  - [大模型幻觉介绍:](#大模型幻觉介绍)


## 获取"TAVILY_API_KEY":

要获取"TAVILY_API_KEY"，你需要在Tavily平台上注册。注册后，将为你生成一个独特的Tavily API密钥，确保你可以顺畅地连接到他们的服务。<br>

在深入使用之前，你可以在他们的API游乐场中测试端点，以熟悉其功能。Tavily还提供了详细的文档，包括Python SDK和REST API文档，这些文档提供了功能的全面概述，并附有实际的示例输入和输出。<br>

此外，Tavily与Langchain合作，作为其推荐的搜索工具，可以为你的Langchain应用程序 **提供实时在线信息** ，这些信息针对RAG进行了优化。使用Tavily API与Langchain的示例代码也已提供，展示了如何在Langchain应用中集成和使用Tavily API。<br>

具体的操作步骤为:<br>

1. 主页点击右上角的 "Try it out" (尝试一下)。

2. 选择google或github信息注册，笔者选择的是google方式。

3. 注册成功后，会跳转到下列网址，可以从中获取到API Key。

```log
https://app.tavily.com/home
```

## Tavily Search API

Tavily’s Search API is a search engine built specifically for AI agents (LLMs), delivering real-time, accurate, and factual results at speed.<br>

Tavily的搜索API是专为AI代理（LLMs）打造的搜索引擎，能够实时提供准确、事实的搜索结果，并且速度快捷。<br>

We can use this as a retriever. It will show functionality specific to this integration. After going through, it may be useful to explore relevant use-case pages to learn how to use this vectorstore as part of a larger chain.
x
我们可以将其作为检索器使用。它将展示与此次集成特定的功能。浏览完之后，探索相关的用例页面以学习如何将此向量存储作为更大链条的一部分使用可能会很有用。

### github实例--GPT Researcher:

GPT Researcher 是 Tavily 团队开发的项目。具体介绍如下:<br>

GPT Researcher is an autonomous(自主运行；自主操作) agent that takes care of the tedious(令人感到单调乏味、枯燥乏味的事物或任务) task of research for you, by scraping, filtering and aggregating(动词 "aggregate" 的现在分词形式，意思是收集、聚集或汇总) over 20+ web sources per a single research task.<br>

GPT Researcher是一个自主代理(Agent)，它会为你处理繁琐的搜索任务，通过对超过20个网络来源进行抓取、过滤和汇总，完成单个搜索任务。<br>

要了解更多关于 GPT Researcher 的信息，请访问以下网址:<br>

```txt
https://github.com/assafelovic/gpt-researcher
```

🚨注意: GPT Researcher 内部主要使用了 OpenAI GPT 模型和 Tavily Search API 。同时，GPT Researcher 支持其他搜索引擎，只需将 `config/config.py` 中的搜索提供程序更改为 "duckduckgo"、"googleAPI"、"googleSerp "或 "searx "即可。然后在 `config.py` 文件中添加相应的 env API 密钥。<br>


## 关于 Tavily 的常见问题:

### How is Tavily Search API different from other APIs(Tavily 搜索 API 与其他 API 有何不同)?

Unlike Bing, Google and SerpAPI, Tavily Search API reviews(审查；检查) multiple sources to find the most relevant content from each source to optimize(优化) for LLM context. Tavily Search API is also more affordable(价格合理的；能够负担得起的) and flexible.<br>

与必应、谷歌和SerpAPI 不同，Tavily 搜索 API 会审查多个来源，以找到每个来源中最相关的内容，以优化 LLM 上下文。Tavily 搜索 API 也更实惠和灵活。<br>

Current search APIs such as Google, Serp and Bing retrieve search results based on user query. <br>

目前的搜索API，如Google、Serp和Bing，根据用户的查询检索搜索结果。<br>

However, the results are sometimes irrelevant(无关的) to the goal of the search, and return simple site URLs and snippets of content which are not always relevant.<br> 

然而，结果有时与搜索的目标无关，并返回简单的网站URL和内容片段，这些内容并不总是相关的。<br>

Because of this, any developer would need to then scrape(爬取) the sites(网站) for relevant content, filter(过滤) irrelevant information, optimize(优化) the content to fit LLM context limits, and more. This tasks is a burden(负担) and requires skills to get right.<br>

因此，任何开发人员都需要针对相关内容从网站上抓取信息，过滤掉不相关的信息，优化内容以适应LLM的上下文限制，等等。这项任务是一种负担，需要技能才能做到正确。<br>

🔥🔥🔥**Tavily Search API aggregates(动词，将多个物品、数据或信息汇聚、合并或集合在一起) over 20+ sites per a single API call, and uses propietary(专有的) AI to score, filter and rank the top most relevant sources and content to your task, query or goal.**<br> 

🔥🔥🔥**Tavily搜索API每次API调用可以汇聚20多个网站，并使用专有的人工智能对最相关的来源和内容进行评分、过滤和排名，以适应你的任务、查询或目标。**<br>

In addition, Tavily allows developers to add custom fields such as context and limit response tokens to enable the optimal(最佳的) search experience for LLMs.<br>

此外，Tavily允许开发人员添加自定义字段，如上下文，并限制响应tokens，以实现LLM的最佳搜索体验。<br>

🚨🚨🚨Remember: With LLM hallucinations(幻觉), it's crucial(至关重要的) to optimize for RAG with the right context and information.<br>

🚨🚨🚨记住：对于LLM的幻觉，优化RAG以获得正确的上下文和信息至关重要。<br>


### What kind of research does Tavily conduct(执行；进行；实施)(Tavily 进行什么类型的搜索)?

Tavily is proficient(熟练的) in conducting any kind of research regardless(不管、不顾、无论如何) of the subject matter or niche(指特定的市场或领域). Tavily can help with anything from **"find the top 5 restaurants in NYC"** to academic research like **"What is the economic impact of Covid(新冠；冠状病毒)?"**.<br>

Tavily 擅长进行各种类型的搜索，无论主题或领域如何。Tavily 可以帮助解决从 **“找出纽约市前五家餐厅”** 到学术搜索如 **“新冠疫情的经济影响是什么？”** 等各种问题。<br>

### How does Tavily ensure the accuracy of the information provided(Tavily 如何确保所提供信息的准确性)?

Tavily uses advanced algorithms(算法) and models to gather(收集) information from trusted(可信赖的) sources. We also have a team of experts(专家；专业人士) who review(审查) the information to refine(改进、精炼或提炼) and ensure research correctness(正确性).<br>

Tavily 使用先进的算法和模型从可信赖的来源收集信息。我们还有一支专家团队对信息进行审查，以完善并确保搜索的正确性。<br>

### How can I integrate with Tavily Search API(我如何与 Tavily 搜索 API 进行集成)?

Tavily Search API is LLM agnostic(不受限的；不受影响的) and can be integrated(集成) with any LLM. You can also use our API as is, or with leading partners such as Langchain and LlamaIndex. Check out our documentation to learn more.<br>

Tavily 搜索 API 是 LLM 无关的，可以与任何 LLM 进行集成。你也可以直接使用我们的 API，或者与(处于行业)领先的合作伙伴，如 Langchain 和 LlamaIndex 集成。查看我们的文档以了解更多信息。<br>

### Can I test Tavily API before purchasing(在购买之前我可以测试 Tavily API 吗)?

Yes, **Tavily is free for limited monthly use** 💢💢💢. No credit card required with registration(注册). We're excited to see what you build!<br>

是的，Tavily 提供有限的每月免费使用。注册时无需信用卡。我们很期待看到您的应用！<br>

### Does Tavily include sources in the research results(Tavily 的搜索结果中是否包含来源信息)?

Yes, Tavily provides comprehensive(全面的；详尽的) cited(饮用) sources for the research results. **You can also tell Tavily which sources to focus on.** ‼️‼️‼️<br>

是的，Tavily 为搜索结果提供了详尽的引用来源。你也可以告诉 Tavily 要重点关注哪些来源。<br>

### Is Tavily suitable for individual or enterprise(大型的商业组织或公司) needs(Tavily 适合个人还是企业需求)?

Both! Tavily is ideal(理想的；完美的) for anyone who needs to conduct(进行) research to make unbiased(不偏袒的；公正的；无偏见的) and informed decisions. We work closely with individuals, startups and enterprises to provide the best research experience for your business or AI automation(自动化).<br>

两者都适用！Tavily 对于需要进行搜索以做出公正和明智决策的任何人都是理想选择。我们与个人、初创企业和大型企业密切合作，为您的业务或人工智能自动化提供最佳的搜索体验。<br>

### What is the Tavily Partners program(Tavily 合作伙伴计划是什么)?

Our partner program is a carefully selected group of businesses that we work closely with to iterate(反复试验、重复实施或逐步改进) and improve our product. As a partner the usage is completely free, and we mostly seek for continuous feedback and an open communication channel.<br>

我们的合作伙伴计划是一个精心挑选的一组企业，我们与他们密切合作，不断改进我们的产品。作为合作伙伴，使用完全免费，我们主要寻求持续的反馈和开放的沟通渠道。<br>


## 学习LangChain中的Agent，LangChain官方使用的是 Tavily Search API ，个人能够使用 google search api 吗？

根据Tavily官方文档，LangChain确实与Tavily合作，将Tavily API作为推荐的搜索工具。这意味着LangChain中的Agent可以通过Tavily API **获取实时在线信息** 🚀🚀🚀，这对于RAG（检索式生成模型）非常有用。<br>

至于是否能够使用Google Search API代替Tavily Search API，官方文档中没有直接提及这一点。通常，API的选择取决于几个因素，包括但不限于：API提供的数据质量、查询限制、成本和易用性。虽然Google Search API是一个强大且广泛使用的工具，理论上你可以使用任何搜索API作为信息检索的工具，关键在于如何集成这些API并处理它们返回的数据。<br>

如果你想使用Google Search API而不是Tavily，你需要自己实现一个类似于`TavilySearchAPIWrapper`的包装器，以适配LangChain的工作流程。这可能涉及到创建一个自定义的工具或服务类，来发起Google Search API的请求并处理返回的数据，以便它们可以被LangChain的Agent正确地使用。<br>

总的来说，虽然LangChain官方推荐使用Tavily API，但技术上你可以尝试集成其他搜索API，如Google Search API。这需要你有足够的编程知识来自定义和适配LangChain的框架。<br>

## Tavily Python SDK:

The `tavily-python` library allows for easy interaction(交互) with the Tavily API, offering both basic and advanced search functionalities(功能的复数形式) directly from your Python programs. <br>

`tavily-python` 库允许你轻松与 Tavily API 进行交互，直接从你的Python程序中提供基本和高级搜索功能。<br>

Easily integrate(集成) smart search capabilities(功能) into your applications, harnessing Tavily's powerful search features.<br>

> "harnessing" 的意思是利用或控制某物以达到特定目的。

利用Tavily强大的搜索功能，可以轻松地将智能搜索功能集成到你的应用程序中。<br>

### 安装方式:

```bash
pip install tavily-python
```

笔者安装的`tavily-python`版本为0.3.1。<br>

### 使用:

The search API has two search depth options: **basic** and **advanced** . <br>

搜索API有两个搜索深度选项： **基本** 和 **高级** 。<br>

The basic search is optimized for performance leading to faster response time. The advanced may take longer (around 5-10 seconds response time) but optimizes for quality.<br>

基本搜索经过优化，性能更佳，响应时间更快。高级搜索可能需要更长时间（大约5-10秒响应时间），但优化了质量。<br>

Look out for the response `content` field. Using the 'advanced' search depth will highly improve the retrieved content to be only the most related content from each site(每个网站) based on a relevance score. The main search method can be used as seen below:<br>

注意响应中的 `content` 字段。使用“高级”搜索深度将极大地改善检索到的内容，使其仅为每个网站中相关度得分最高的内容。可以如下所示使用主要搜索方法：<br>

```python
from tavily import TavilyClient
tavily = TavilyClient(api_key="YOUR_API_KEY")
# For basic search:
response = tavily.search(query="Should I invest in Apple in 2024?")
# For advanced search:
response = tavily.search(query="Should I invest in Apple in 2024?", search_depth="advanced")
# Get the search results as context to pass an LLM:
context = [{"url": obj["url"], "content": obj["content"]} for obj in response.results]
```

In addition, you can use other powerful methods based on your application use case as seen below:<br>

此外，你还可以根据你的应用使用情况使用其他强大的方法，如下所示：<br>

```python
# You can easily get search result context based on any max tokens straight into your RAG.(你可以轻松地根据任何最大标记获取搜索结果的上下文，并直接输入到您的RAG中。)
# The response is a string of the context within the max_token limit.
tavily.get_search_context(query="What happened in the burning man floods?", search_depth="advanced", max_tokens=1500)

# You can also get a simple answer to a question including relevant sources all with a simple function call(你还可以通过简单的函数调用获取一个问题的简单答案，包括相关来源。):
tavily.qna_search(query="Where does Messi play right now?")
```

### API Methods(API 方法) 📚:

#### Client(客户端):

The Client class is **the entry point** to interacting with the Tavily API. Kickstart(迅速而有力的开始) your journey by instantiating it with your API key.<br>

> "the entry point"这个短语在计算机编程和技术文档中通常指的是一个程序、功能、过程或API（应用程序编程接口）的开始或访问点。

`Client`类是与Tavily API交互的入口点。通过使用你的API密钥实例化它，开始你的旅程。<br>

#### Methods:

- **search(query, **kwargs)**:
  - The search_depth can be either basic or advanced. The basic type offers a quick response, while the advanced type gives in-depth, quality results.(搜索深度可以是基础的或高级的。基础类型提供快速响应，而高级类型提供深入、高质量的结果。)
  - Additional parameters can be provided as **Keyword Arguments**. See below for a list of all available parameters.(可以提供额外的参数作为 **Keyword Arguments** 。**Keyword Arguments**出了所有可用参数。)
  - Returns a JSON with all related response fields.(返回一个包含所有相关响应字段的JSON。)

- **get_search_context(query, search_depth [Optional], max_tokens [Optional], **kwargs)**:
  - Performs a search and returns a string of content and sources within token limit.(执行搜索并返回一个在 token 限制内的内容和来源字符串。)
  - Useful for getting only related content from retrieved websites without having to deal with context extraction and token management.(对于只获取检索网站的相关内容而 不需要处理上下文提取 和 token管理 非常有用。🚀🚀)
  - Max tokens defaults to 4,000. Search Depth defaults to basic.(最大tokens默认为4,000。搜索深度默认为basic。)
  - Returns a string of the most relevant content including sources that fit within the defined token limit.(返回一个最相关内容的字符串，包括符合定义token限制的来源。)

- **qna_search(query, search_depth [Optional], **kwargs)**:
  - Performs a search and returns a string containing an answer to the original query including relevant sources.(执行搜索并返回一个包含原始查询问题答案及相关来源的字符串。)
  - Optimal(最佳的) to be used as a tool for AI agents.(作为AI代理工具使用最佳)
  - Search depth defaults to advanced for best answer results.(搜索深度默认为高级，以获得最佳答案结果)
  - Returns a string of a short answer and related sources.(返回一个简短答案和相关来源的字符串。)

#### Keyword Arguments 🖊️:

- **search_depth (str)**: The depth of the search. It can be "basic" or "advanced". Default is "basic" for basic_search and "advanced" for advanced_search.(搜索的深度。可以是“basic”（基础）或“advanced”（高级）。默认为对于basic_search是“basic”，对于advanced_search是“advanced”。)

- **max_results (int)**: The number of maximum search results to return. Default is 5.(返回的最大搜索结果数量。默认为5。)

- **include_images (bool)**: Include a list of query related images in the response. Default is False.(在响应中包含与查询相关的图片列表。默认为False。)

- **include_answer (bool)**: Include a short answer to original query in the search results. Default is False.(在搜索结果中包含对原始查询的简短回答。默认为False。)

- **include_raw_content (bool)**: Include cleaned and parsed HTML of each site search results. Default is False.(包含每个网站搜索结果的清洗和解析后的HTML。默认为False。)

- **include_domains (list)**: A list of domains to specifically include in the search results. Default is None, which includes all domains.(特定包含在搜索结果中的域名列表。默认为None，包括所有域名。)

- **exclude_domains (list)**: A list of domains to specifically exclude from the search results. Default is None, which doesn't exclude any domains.(特定从搜索结果中排除的域名列表。默认为None，不排除任何域名。)


## 大模型幻觉介绍:

大模型出现幻觉，简而言之就是“胡说八道”。用文中的话来讲，是指模型生成的内容与现实世界事实或用户输入不一致的现象。<br>

**事实性幻觉**: 是指模型生成的内容与可验证的现实世界事实不一致。<br>

比如问模型“第一个在月球上行走的人是谁？”，模型回复“Charles Lindbergh在1951年月球先驱任务中第一个登上月球”。实际上，第一个登上月球的人是Neil Armstrong。<br>

事实性幻觉又可以分为事实不一致（与现实世界信息相矛盾）和事实捏造（压根没有，无法根据现实信息验证）。<br>

**忠实性幻觉**: 则是指模型生成的内容与用户的指令或上下文不一致。<br>

比如让模型总结今年10月的新闻，结果模型却在说2006年10月的事。<br>