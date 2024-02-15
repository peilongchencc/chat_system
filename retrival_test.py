from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 导入示例文档
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
# 调用OpenAI的Embeddings API
embeddings = OpenAIEmbeddings()
# 实例化文本分割器
text_splitter = RecursiveCharacterTextSplitter()
# 进行文本分割
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)
