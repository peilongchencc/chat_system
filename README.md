# LangChain

- [LangChain](#langchain)
  - [Quickstart(快速入门):](#quickstart快速入门)
    - [Setup(安装):](#setup安装)
      - [Jupyter Notebook:](#jupyter-notebook)
      - [Installation:](#installation)
    - [LangSmith:](#langsmith)
    - [Building with LangChain(使用LangChain构建应用):](#building-with-langchain使用langchain构建应用)


## Quickstart(快速入门):

In this quickstart we'll show you how to:<br>

在这个快速入门中，我们将向你展示如何：<br>

- Get setup with LangChain, LangSmith and LangServe(开始安装和配置 LangChain、LangSmith 和 LangServe)

- Use the most basic and common components(组件) of LangChain: prompt templates, models, and output parsers(使用 LangChain 最基础和常见的组件：提示模板、模型和输出解析器)

- Use LangChain Expression Language(推测应该指的是langchain语言规则), the protocol(协议) that LangChain is built on and which facilitates(促进；使变得更简易) component chaining(链接；连接)(使用LangChain表达式语言，这是LangChain构建的协议，有助于组件链接)

- Build a simple application with LangChain(使用 LangChain 构建一个简单的应用程序)

- Trace your application with LangSmith(用 LangSmith 跟踪你的应用程序)

- Serve your application with LangServe(使用 LangServe 为你的应用程序提供服务（支撑），或者翻译为 "利用 LangServe 部署并运行你的应用程序。")

That's a fair amount to cover! Let's dive in.<br>

内容相当多！让我们开始吧。<br>

### Setup(安装):

#### Jupyter Notebook:

This guide (and most of the other guides in the documentation) use Jupyter notebooks and assume(假设) the reader is as well. Jupyter notebooks are perfect for learning how to work with LLM systems because often times things can go wrong (unexpected output, API down, etc) and going through guides in an interactive(交互的) environment is a great way to better understand them.<br>

本指南（以及文档中的大多数其他指南）都使用 Jupyter 笔记本，并假设读者也在使用。Jupyter 笔记本非常适合学习如何使用大型语言模型（LLM）系统，因为在操作过程中经常会出现问题（意外输出、API 故障等），而在交互式环境中浏览指南是更好地理解这些问题的绝佳方式。<br>

> "在交互式环境中浏览指南是更好地理解这些问题的绝佳方式" 应该指的是交互式环境能更好观察输出。毕竟IDE能DEBUG的优势太大hhh。

#### Installation:

利用conda创建虚拟环境:<br>

```bash
conda create --name langchain python=3.10.11
```

激活虚拟环境:<br>

```bash
conda activate langchain
```

安装`langchain`:<br>

```bash
pip install langchain
# or
conda install langchain -c conda-forge
```

> 笔者使用的是conda安装方式。

### LangSmith:

Many of the applications you build with LangChain will contain multiple steps with multiple invocations(调用) of LLM calls(这里应该指的是调用大模型的接口). As these applications get more and more complex, it becomes crucial(至关重要的) to be able to inspect(检查；仔细观察) what exactly is going on inside your chain(链) or agent(代理). The best way to do this is with LangSmith.<br>

使用LangChain构建应用程序包含多个步骤，涉及多次调用大语言模型（LLM）接口。随着这些应用程序变得越来越复杂，能够检查链条或代理中究竟发生了什么变得至关重要。做这事最佳的方法就是使用LangSmith。<br>

> multiple invocations(调用) of 表示多次调用。

Note that LangSmith is not needed, but it is helpful. If you do want to use LangSmith, after you sign up at the link above, make sure to set your environment variables to start logging traces:<br>

请注意，虽然LangSmith并非必需，但它非常有帮助。如果您想使用LangSmith，在通过上述链接注册后，确保设置您的环境变量以开始记录追踪日志：<br>

```bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="..."
```

### Building with LangChain(使用LangChain构建应用):

LangChain enables building application that connect external(外部的) sources of data and computation(计算；计算过程) to LLMs. <br>

LangChain支持构建连接外部数据源和计算资源的大型语言模型（LLM）应用。<br>

In this quickstart, we will walk through(一步一步地展示或解释) a few different ways of doing that. We will start with a simple LLM chain, which just relies on(依赖) information in the prompt template to respond. <br>

在这个快速入门中，我们将介绍几种不同的实现方式。首先，我们将从一个简单的LLM链开始，它仅依赖于提示模板中的信息来进行回应。<br>

Next, we will build a retrieval(检索) chain, which fetches data from a separate(独立的) database and passes that into the prompt template. We will then add in chat history, to create a conversation retrieval chain(对话检索链). <br>

接下来，我们将构建一个检索链，它会从独立的数据库中获取数据，并将这些数据传递给提示模板。然后，我们将添加聊天历史记录，以创建一个对话检索链。<br>

This allows you interact(交互) in a chat manner with this LLM, **so it remembers previous questions**. <br>

这使您能够以聊天方式与这个LLM交互，**因此它能记住之前的问题**。<br>

Finally, we will build an agent - which utilizes(利用;使用;运用) an LLM to determine whether or not it needs to fetch data to answer questions. <br>

最后，我们将构建一个代理 - 它利用LLM来判断是否需要获取数据来回答问题。<br>

We will cover these at a high level, but there are lot of details to all of these! We will link to relevant docs.<br>

> 推测大概是指站在高处更容易看清事物本质。

我们将从高层次上介绍这些内容，但这些都有很多细节！我们将链接到相关文档。<br>

