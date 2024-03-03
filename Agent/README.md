# Agents(代理):
- [Agents(代理):](#agents代理)
  - [Quickstart(快速入门):](#quickstart快速入门)
    - [Setup: LangSmith(设置：LangSmith)](#setup-langsmith设置langsmith)
    - [Define tools(定义工具):](#define-tools定义工具)
      - [Tavily](#tavily)
    - [Retriever(检索器):](#retriever检索器)
    - [Tools:](#tools)
    - [Create the agent(创建代理):](#create-the-agent创建代理)
    - [Run the agent:](#run-the-agent)
    - [Agent 逻辑理解：](#agent-逻辑理解)
      - [模拟问题:](#模拟问题)
      - [Agent运行逻辑:](#agent运行逻辑)
  - [Concepts(概念):](#concepts概念)
  - [Agent Types(代理类型):](#agent-types代理类型)
  - [Tools(工具):](#tools工具)
  - [How To Guides(操作指南):](#how-to-guides操作指南)

The core idea(核心理念) of agents is to use a language model to choose a sequence of actions to take.<br>

**代理的核心理念是利用语言模型选择一系列要执行的动作。** <br>

In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used **as a reasoning engine** to determine which actions to take and in which order.<br>

在链式编程中，一系列动作是硬编码的（在代码中）。而在代理中，语言模型 **被用作推理引擎** ，确定要采取的动作及其顺序。<br>

## Quickstart(快速入门):

For a quick start to working with agents, please check out [this getting started guide](https://python.langchain.com/docs/modules/agents/quick_start). This covers basics like **initializing an agent**, **creating tools**, and **adding memory**.<br>

要快速开始使用代理，请查看此入门指南。其中包括**初始化代理**、**创建工具**和**添加记忆**等基础知识。<br>

Quickstart(快速入门)原文:<br>

To best understand the agent framework, let’s build an agent that has two tools: one to look things up online(在线的), and one to look up specific data that we’ve loaded into a index.<br>

为了最好地理解代理框架，让我们建立一个代理，其中包含两个工具：一个用于在线查找信息，另一个用于查找我们加载到索引中的特定数据。<br>

This will assume(假设) knowledge of LLMs and retrieval so if you haven’t already explored those sections, it is recommended you do so.<br>

这将假设您已经了解了LLMs和检索，如果您还没有探索这些部分，建议您这样做。<br>

### Setup: LangSmith(设置：LangSmith)

By definition, agents take a self-determined(自我确定的；自我决定的), input-dependent sequence of steps before returning a user-facing output.<br>

根据定义，代理在返回用户可见的输出之前需要执行一系列自我确定的、依赖输入的步骤。<br>

This makes debugging these systems particularly tricky, and observability particularly important. LangSmith is especially useful for such cases.<br>

这使得调试这些系统特别棘手，而观察性特别重要。LangSmith 在这种情况下特别有用。<br>

When building with LangChain, all steps will automatically(自动的) be traced(追踪) in LangSmith. To set up LangSmith we just need set the following environment variables:<br>

在使用 LangChain 构建时，所有步骤将自动在 LangSmith 中被追踪。要设置 LangSmith，我们只需要设置以下环境变量：<br>

```bash
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="<your-api-key>"
```

### Define tools(定义工具):

We first need to create the tools we want to use. We will use two tools: `Tavily` (to search online) and then a `retriever` over a local index we will create.<br>

首先，我们需要创建我们想要使用的工具。我们将使用两个工具：Tavily（用于在线搜索）和一个我们将要创建的本地索引检索器。<br>

#### Tavily

We have a built-in tool in LangChain to easily use Tavily search engine as tool. <br>

在LangChain中，我们内置了工具，可以轻松地使用Tavily搜索引擎作为工具。<br>

Note that this requires an API key - they have a free tier(原意:等；层级。在这里意味着不同的服务等级或套餐), but if you don’t have one or don’t want to create one, you can always ignore this step.<br>

请注意，这需要一个API密钥 - 他们提供免费套餐，但如果你没有密钥或不想创建一个，你可以忽略这一步。<br>

Once you create your API key, you will need to export that as:<br>

一旦你创建了你的API密钥，你将需要将其导出为：<br>

```bash
export TAVILY_API_KEY="..."
```

代码如下:<br>

```python
from langchain_community.tools.tavily_search import TavilySearchResults
search = TavilySearchResults()
print(search.invoke("what is the weather in SF"))
```

终端输出:<br>

```txt
[{'url': 'https://www.metoffice.gov.uk/weather/forecast/9q8yym8kr',
  'content': 'Thu 11 Jan Thu 11 Jan Seven day forecast for San Francisco  San Francisco (United States of America) weather Find a forecast  Sat 6 Jan Sat 6 Jan Sun 7 Jan Sun 7 Jan Mon 8 Jan Mon 8 Jan Tue 9 Jan Tue 9 Jan Wed 10 Jan Wed 10 Jan Thu 11 Jan  Find a forecast Please choose your location from the nearest places to : Forecast days Today Today Sat 6 Jan Sat 6 JanSan Francisco 7 day weather forecast including weather warnings, temperature, rain, wind, visibility, humidity and UV ... (11 January 2024) Time 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00 08:00 09:00 10:00 11:00 12:00 ... Oakland Int. 11.5 miles; San Francisco International 11.5 miles; Corte Madera 12.3 miles; Redwood City 23.4 miles;'},
 {'url': 'https://www.latimes.com/travel/story/2024-01-11/east-brother-light-station-lighthouse-california',
  'content': "May 18, 2023  Jan. 4, 2024 Subscribe for unlimited accessSite Map Follow Us MORE FROM THE L.A. TIMES  Jan. 8, 2024 Travel & Experiences This must be Elysian Valley (a.k.a. Frogtown) Jan. 5, 2024 Food  June 30, 2023The East Brother Light Station in the San Francisco Bay is not a destination for everyone. ... Jan. 11, 2024 3 AM PT ... Champagne and hors d'oeuvres are served in late afternoon — outdoors if ..."}]
```

### Retriever(检索器):

We will also create a retriever over some data of our own. For a deeper explanation of each step here, see [this section](https://python.langchain.com/docs/modules/data_connection/).<br>

我们还将针对我们自己的一些数据创建一个检索器。要深入了解这里每一步的更多解释，请参阅本节。<br>

```python
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vector.as_retriever()
print(retriever.get_relevant_documents("how to upload a dataset")[0])
```

终端输出:<br>

```python
Document(page_content="dataset uploading.Once we have a dataset, how can we use it to test changes to a prompt or chain? The most basic approach is to run the chain over the data points and visualize the outputs. Despite technological advancements, there still is no substitute for looking at outputs by eye. Currently, running the chain over the data points needs to be done client-side. The LangSmith client makes it easy to pull down a dataset and then run a chain over them, logging the results to a new project associated with the dataset. From there, you can review them. We've made it easy to assign feedback to runs and mark them as correct or incorrect directly in the web app, displaying aggregate statistics for each test project.We also make it easier to evaluate these runs. To that end, we've added a set of evaluators to the open-source LangChain library. These evaluators can be specified when initiating a test run and will evaluate the results once the test run completes. If we’re being honest, most of", metadata={'source': 'https://docs.smith.langchain.com/overview', 'title': 'LangSmith Overview and User Guide | 🦜️🛠️ LangSmith', 'description': 'Building reliable LLM applications can be challenging. LangChain simplifies the initial setup, but there is still work needed to bring the performance of prompts, chains and agents up the level where they are reliable enough to be used in production.', 'language': 'en'})
```

Now that we have populated(填充) our index that we will do doing retrieval over, we can easily turn it into a tool (the format needed for an agent to properly(正确的；合适的) use it).<br>

现在我们已经填充了我们将要进行检索的索引，我们可以轻松地将其转换为一个工具（代理程序正确使用所需的格式）。<br>

```python
from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)
```

### Tools:

Now that we have created both, we can create a list of tools that we will use downstream.<br>

既然我们已经创建了两者，我们可以创建一个我们将在下游使用的工具列表。<br>

```python
tools = [search, retriever_tool]
```

### Create the agent(创建代理):

Now that we have defined the tools, we can create the agent. We will be using an OpenAI Functions agent - for more information on this type of agent, as well as other options, see [this guide](https://python.langchain.com/docs/modules/agents/agent_types).<br>

既然我们已经定义了工具，我们可以创建代理程序。我们将使用 OpenAI Functions 代理程序 - 关于这种类型的代理程序以及其他选项的更多信息，请参阅此指南。<br>

First, we choose the LLM we want to be guiding the agent.<br>

首先，我们选择要指导代理程序的语言模型。<br>

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

Next, we choose the prompt we want to use to guide the agent.<br>

接下来，我们选择要用来指导代理程序的提示语。<br>

If you want to see the contents of this prompt and have access to LangSmith, you can go to:<br>

如果您想查看此提示语的内容并访问 LangSmith，您可以前往：<br>

```txt
https://smith.langchain.com/hub/hwchase17/openai-functions-agent
```

```python
from langchain import hub

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt.messages)
```

终端输出:<br>

```txt
[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], template='You are a helpful assistant')),
 MessagesPlaceholder(variable_name='chat_history', optional=True),
 HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], template='{input}')),
 MessagesPlaceholder(variable_name='agent_scratchpad')]
```

Now, we can initalize the agent with the LLM, the prompt, and the tools. <br>

现在，我们可以用语言模型、提示语和工具初始化代理程序。<br>

The agent is responsible(负责) for taking in input and deciding what actions to take.<br>

代理程序负责接收输入并决定采取什么行动。<br>

Crucially, the Agent does not execute those actions - that is done by the AgentExecutor (next step).<br>

> "Crucially" 是一个副词，意思是“至关重要地”或“关键地”。它强调某事的重要性或关键性。读音为 /ˈkruːʃəli/。

关键是，代理程序不执行这些行动 - 这是由代理执行器（下一步）完成的。<br>

For more information about how to think about these components, see our [conceptual guide](https://python.langchain.com/docs/modules/agents/concepts).<br>

有关如何考虑这些组件的更多信息，请参阅我们的概念指南。<br>

```python
from langchain.agents import create_openai_functions_agent

agent = create_openai_functions_agent(llm, tools, prompt)
```

Finally, we combine the agent (the brains) with the tools inside the AgentExecutor (which will repeatedly(反复的) call the agent and execute tools). For more information about how to think about these components, see our conceptual guide.<br>

最后，我们将代理程序（即大脑）与 AgentExecutor 中的工具组合在一起（AgentExecutor 将反复调用代理程序并执行工具）。有关如何考虑这些组件的更多信息，请参阅我们的概念指南。<br>

```python
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

### Run the agent:

We can now run the agent on a few queries! Note that for now, these are all stateless queries (it won’t remember previous interactions).<br>

我们现在可以在一些查询上运行这个代理了！请注意，目前这些都是无状态的查询（它不会记住之前的互动）。<br>

```python
agent_executor.invoke({"input": "hi!"})
```

终端输出:<br>

```python
> Entering new AgentExecutor chain...
Hello! How can I assist you today?

> Finished chain.
```

### Agent 逻辑理解：

#### 模拟问题:

LangChain中利用gpt-3.5作为llm，当用户输入问题后，有2种预设的工具。一种是连网查找、爬取相关内容；一种是基本已有文档回答特定领域知识，例如橄榄球领域。那么Agent是如何工作的？<br>

#### Agent运行逻辑:

当LangChain的Agent接收到用户输入后，它首先会利用大型语言模型（LLM）进行一个分类任务，以判断最适合的处理策略。这个分类步骤是至关重要的，因为它决定了Agent接下来将采取哪种方式来寻找或生成答案。具体来说，这个过程通常包括以下几个判断和步骤：<br>

1. **理解用户的请求**：通过分析用户的输入，LangChain的Agent首先尝试理解请求的本质，包括问题的领域、复杂性以及所需的信息类型。

2. **分类任务**：基于对用户请求的理解，Agent使用LLM进行分类，判断如何最有效地回答这个问题。分类结果大致分为以下几种情况：
  - **连网查找**：如果问题需要当前的或者特定的数据，或者是超出LLM知识截止日期的信息，Agent决定执行连网查找。
  - **特定领域知识回复**：对于某些专业领域的问题，如果Agent有预先准备的特定领域知识库，如橄榄球相关的知识，它会选择从这些文档中寻找答案。
  - **常规回复**：对于不需要外部信息来源的问题，比如一般性知识问题、解释性问题或建议性问题，Agent会直接利用LLM的内置知识库生成回答。

3. **执行对应策略**：一旦分类完成，Agent会根据分类结果采取相应的行动。这可能涉及到查询内部数据库、执行网络搜索或者直接利用LLM的知识生成答案。

4. **生成和提供回答**：无论采取哪种策略，最终Agent都会生成一个回答，整合所得的信息（如果进行了搜索或查询特定文档的话），并以用户可理解的格式提供回答。

这个过程展示了LangChain如何结合大型语言模型的理解能力和多种策略来处理各种类型的用户请求，从而提供准确和及时的回答。<br>


## Concepts(概念):

There are several key concepts to understand when building agents: Agents, AgentExecutor, Tools, Toolkits(工具包). For an in depth explanation, please check out [this conceptual(与概念相关的、基于概念的、涉及概念的) guide](https://python.langchain.com/docs/modules/agents/concepts).<br>

构建代理时有几个关键概念需要理解：代理、代理执行器、工具和工具包。要深入了解，请查看这个概念指南。<br>


## Agent Types(代理类型):

There are many different types of agents to use. For a overview of the different types and when to use them, please check out [this section](https://python.langchain.com/docs/modules/agents/agent_types/).<br>

有许多不同类型的代理可供使用。要了解不同类型(的代理)及其使用时机，请查看本节。<br>


## Tools(工具):

Agents are only as good as the tools they have. For a comprehensive(全面的) guide on tools, please see [this section](https://python.langchain.com/docs/modules/agents/tools/).<br>

代理的好坏取决于它们拥有的工具。要获得关于工具的全面指南，请参阅本节。<br>


## How To Guides(操作指南):

> "How To Guides" 表面的意思是 "如何指南" ，我们通常用的它的延伸含义 "操作指南"。

Agents have a lot of related functionality! Check out comprehensive guides including(代理有许多相关功能！查看包括以下内容的全面指南：):<br>

- [Building a custom agent(构建自定义代理)](https://python.langchain.com/docs/modules/agents/how_to/custom_agent)

- [Streaming of both intermediate(中间的) steps and tokens(流式处理（包括中间步骤和标记的流式处理）)](https://python.langchain.com/docs/modules/agents/how_to/streaming)

- Building an agent that returns structured output(构建返回结构化输出的代理)

- Lots functionality around using AgentExecutor, including: using it as an iterator, handle parsing errors, returning intermediate steps, capping the max number of iterations, and timeouts for agents。(还有很多关于使用代理执行器的功能，包括：将其用作迭代器、处理解析错误、返回中间步骤、限制最大迭代次数以及代理的超时。)
