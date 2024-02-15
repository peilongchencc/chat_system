请将下列内容翻译为地道的中文：

### Retrieval Chain(检索链--查找并提取的过程):

In order to properly(恰当的) answer the original(原始的) question ("how can langsmith help with testing?"), we need to provide additional(额外的) context to the LLM.<br>

为了恰当回答原始问题（"langsmith 如何帮助进行测试？"），我们需要向 LLM 提供额外的上下文。<br>

 We can do this via retrieval. Retrieval is useful when you have too much data to pass to the LLM directly(直接地)(too..to... 太...而不能...). You can then use a retriever to fetch only the most relevant pieces(最相关的片段) and pass those in.<br>



In this process, we will look up relevant documents from a Retriever and then pass them into the prompt. A Retriever can be backed by anything - a SQL table, the internet, etc - but in this instance we will populate a vector store and use that as a retriever. For more information on vectorstores, see this documentation.

First, we need to load the data that we want to index. In order to do this, we will use the WebBaseLoader. This requires installing BeautifulSoup:

这可以通过检索来实现。当你有太多数据不能直接传递给 LLM 时，检索非常有用。你可以使用检索器只获取最相关的数据片段然后传入。

在这个过程中，我们将从检索器中查找相关文档，然后将它们传入提示中。检索器可以由任何东西支持——一个 SQL 表，互联网等——但在这个例子中，我们将填充一个向量存储并使用它作为检索器。有关向量存储的更多信息，请参阅此文档。

首先，我们需要加载我们想要索引的数据。为了做到这一点，我们将使用 WebBaseLoader。这需要安装 BeautifulSoup：