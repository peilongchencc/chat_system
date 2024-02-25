import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from load_file_split_documents import ChineseRecursiveTextSplitter
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'

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
print(vector)
