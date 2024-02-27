"""
@author:PeilongChen(peilongchencc@163.com)
@description:实现基于LangChain的文档检索链。
"""
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from load_file_split_documents import ChineseRecursiveTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'


########################################################################
# 文档切分，进行向量化，并存入FAISS
########################################################################

chunk_overlap = 50
chunk_size = 500
# 替换为你的文件路径
filepath = 'example_data.txt'
# 使用LangChain内置txt文件加载器
loader = TextLoader(filepath)
# 使用加载器加载文档
docs = loader.load()    # 数据类型为list [(page_content='（一）直接打压式\n洗盘\n直接打压较多出现在 庄家 吸货区域，目的是... metadata={'source': 'example_data.txt'}' metadata={'source': 'example_data.txt'})]
# 调用OpenAI的Embeddings API
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
# 实例化自定义的文本分割器
text_splitter = ChineseRecursiveTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
# 进行文本分割
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

########################################################################
# 调用大模型(接口)，构建prompt
########################################################################

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    # model_name="gpt-4-0125-preview"
    )
# 让模型 "仅根据提供的上下文回答以下问题"
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)  # "input" 和 "context" 参数会从 `.invoke()` 的参数中获取。

########################################################################
# 构建检索链
########################################################################

retriever = vector.as_retriever()

retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "横盘整理的形态是什么样子?"})   # L2 distance in float. Lower score represents more similarity.

print(response["answer"])

# 由于结果含有随机性，笔者终端见到的2种回复如下:
# 回复1: 横盘整理的形态在K线上的表现常常是一条横线或者长期的平台。
# 回复2: 横盘整理的形态在K线上的表现常常是一条横线或者长期的平台，从成交量上来看，在平台整理的过程中成交量呈递减的状态。也就是说，在平台上没有或很少有成交量放出。成交清淡，成交价格也极度不活跃。