import os
from datasets import load_dataset
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('钛学术_期刊_人工智能技术在档案管理中的应用.pdf')
pages = loader.load_and_split()
print(pages)