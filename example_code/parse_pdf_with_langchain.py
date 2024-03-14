"""
@author:ChenPeilong(peilongchencc@163.com)
@description:LangChain解析PDF文件示例,双栏PDF可解析。
@Prerequisite for use:pip install pypdf
@reference link:https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf
"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('钛学术_期刊_人工智能技术在档案管理中的应用.pdf')
pages = loader.load_and_split()
print(pages)