# LangChain

本项目基于LangChain官网翻译、添加自己的理解，主要用于个人研究、学习。<br>

- [LangChain](#langchain)
  - [Quickstart(快速入门):](#quickstart快速入门)
    - [Setup(安装):](#setup安装)
      - [Jupyter Notebook:](#jupyter-notebook)
      - [Installation:](#installation)
    - [LangSmith:](#langsmith)
    - [Building with LangChain(使用LangChain构建应用):](#building-with-langchain使用langchain构建应用)
    - [LLM Chain:](#llm-chain)
      - [OpenAI:](#openai)


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

### LLM Chain:

For this getting started guide, we will provide two options: using OpenAI (a popular model available via API) or using a local open source model.<br>

对于这个入门指南，我们将提供两种选择：使用 OpenAI（一种可以通过 API 调用的流行模型）或使用本地开源模型。<br>

#### OpenAI:

First we'll need to import the LangChain x OpenAI integration(集成) package.<br>

首先，我们需要导入 LangChain 与 OpenAI 的集成包。<br>

```bash
pip install langchain-openai
```

Accessing the API requires an API key, which you can get by creating an account(账户) and heading(前往) [here](https://platform.openai.com/api-keys). Once we have a key we'll want to set it as an environment variable by running:<br>

要访问 API，你需要一个 API 密钥，可以通过创建一个账户并前往这里来获取。一旦我们拥有了密钥，我们会想要通过运行以下命令将其设置为一个环境变量：<br>

```bash
export OPENAI_API_KEY="your-api-key-here"
```

We can then initialize the model:<br>

然后我们可以初始化模型：<br>

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
```

If you'd prefer not to set an environment variable you can pass the key in directly(直接地) via the `openai_api_key` named parameter when initiating the OpenAI LLM class:<br>

如果你不想设置环境变量，你可以在初始化 OpenAI LLM 类时，直接通过 openai_api_key 这个命名参数传入密钥：<br>

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_key="...")
```

Once you've installed and initialized the LLM of your choice, we can try using it!<br>

一旦你安装并初始化了你选择的 LLM，我们就可以尝试使用它了！<br>

Let's ask it what LangSmith is - this is something that wasn't present in the training data so it shouldn't have a very good response.<br>

让我们问问它 LangSmith 是什么 - 这是训练数据中没有的内容，所以它应该不会有很好的回答。<br>

```python
llm.invoke("how can langsmith help with testing?")
```

> 在编程领域，"invoke a function" 表示 "调用一个函数"，所以上述代码中 "invoke" 的意思大概率是 "调用"。

笔者在IDE中测试的效果如下:<br>

> 必须保证终端能够连接openai服务，才可以使用以下代码。
> 经测试，运行`llm.invoke("...")`后终端以非流式输出形式返回。

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm_response = llm.invoke("你好")

print(llm_response)     # content='你好！有什么我可以帮助你的吗？'
print(type(llm_response))   # <class 'langchain_core.messages.ai.AIMessage'>
print(llm_response.content) # 你好！有什么我可以帮助你的吗？
```

We can also guide(指导；引导) it's response with a prompt template(模板). Prompt templates are used to convert(转换) raw user input to a better input to the LLM.<br>

我们还可以使用提示模板来引导其回应。提示模板用于将原始用户输入转换为更适合语言模型（LLM）的输入。

```python
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),  # 英文的意思是: 你是世界级的技术文档撰写专家(写手)。
    ("user", "{input}")
])
```

We can now combine these into a simple LLM chain:<br>

现在，我们可以将这些组合成一个简单的LLM链：<br>

```python
chain = prompt | llm 
```

We can now invoke(调用) it and ask the same question. It still won't know the answer, but it should respond(回应) in a more proper tone for a technical writer!<br>

现在我们可以调用它并询问相同的问题。它仍然不会知道答案，但应该以更适合技术写手的语气回应！<br>

```python
chain.invoke({"input": "how can langsmith help with testing?"})
```

笔者所用的完整代码如下:<br>

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm 

chain_response = chain.invoke({"input": "how can langsmith help with testing?"})

print(chain_response.content)
```

The output of a ChatModel (and therefore, of this chain) is a message. However, it's often much more convenient to work with strings. Let's add a simple output parser to convert the chat message to a string.<br>

> "and therefore, of this chain" 这个短语的意思是 "因此，对于这个链也是如此"。搞不懂 "因此，对于这个链也是如此" 在这句话中的含义，但不妨碍整句话的理解。

ChatModel（因此，对于这个链也是如此）的输出是一条消息。然而，使用字符串通常更方便。让我们添加一个简单的输出解析器，将聊天消息转换为字符串。<br>

```python
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
```

We can now add this to the previous(之前的) chain:<br>

现在我们可以将这个添加到之前的链中：<br>

```python
chain = prompt | llm | output_parser
```

We can now invoke(调用) it and ask the same question. The answer will now be a string (rather than a ChatMessage).<br>

现在我们可以调用它并提出同样的问题。现在的答案将是一个字符串（而不是ChatMessage）。<br>

```python
chain.invoke({"input": "how can langsmith help with testing?"})
```

笔者所用完整代码:<br>

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

chain_response = chain.invoke({"input": "how can langsmith help with testing?"})

print(chain_response)
print(type(chain_response))     # <class 'str'>
```

这次添加了结果解析器，输出的直接是 `string` 类型的结果，其实和之前笔者使用的 `print(chain_response.content)` 效果相同。<br>

