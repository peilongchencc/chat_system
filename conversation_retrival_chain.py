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
from langchain_core.messages import HumanMessage, AIMessage
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder

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
retriever = vector.as_retriever()

########################################################################
# 调用大模型(接口)，构建prompt
########################################################################

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    # model_name="gpt-4-0125-preview"
    )

########################################################################
# 第一次调用llm，将多轮对话中当前问句的信息补充完整(如果当前问句缺少信息的话，例如缺主语等等。)
########################################################################

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
])
# 构建检索器链, "create history aware retriever" 表示创建一个具有历史意识的检索器,aware表示意识到或知道某种情况。
retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

########################################################################
# 第二次调用llm，利用刚刚生成的含完整信息的问句从文档中检索需要的内容
########################################################################

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])
document_chain = create_stuff_documents_chain(llm, prompt)
# 构建检索链
retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

# chat_history_content = "横盘整理的形态是什么样子?"

file_path = "financial_data.txt"

with open(file_path, "r") as file:
    chat_history_content = file.read()

chat_history = [HumanMessage(content=chat_history_content), AIMessage(content="Yes!")]
print(chat_history)

response = retrieval_chain.invoke({
    "chat_history": chat_history,
    "input": "可转债具备债性吗？"
})

print(response["answer"])

# 终端输出:
# 这种情况出现的原因是主力在股价上升到敏感价位或者市场背景有所转换时，会适时抛出一部分筹码，打压住股价的上升趋势，形成平台整理的格局。在这个阶段内，成交量稍显活跃，一旦平台整理格局形成，成交量会迅速萎缩。

# 原文:
# 横盘整理的形态在K线上的表现常常是一条横线或者长期的平台，从成交量上来看，在平台整理的过程中成交量呈递减的状态。也就是说，在平台上没有或很少有成交量放出。成交清淡，成交价格也极度不活跃。为什么会出现这种情况呢？其内在的机理就是：当股价上升到敏感价位或浮码涌动亦或市场背景有所转换的时候，主力会适时抛出一部分筹码，打压住股价的升势，用一部分资金顶住获利抛盘，强制股价形成平台整理的格局，在这个阶段内，成交量稍显活跃，一旦平台整理格局形成，成交量应迅速地萎缩下来。主力一般会让散户投资者和小资金持有者所持筹码在平台内充分自由换手，只是在大势不好股价下滑的情况下，适时控制股价下跌的冲动。此阶段时间内的成交量由于主力活动极少，成交量应该是清淡的。