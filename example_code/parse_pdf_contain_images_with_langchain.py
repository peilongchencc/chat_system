"""
@author:ChenPeilong(peilongchencc@163.com)
@description:LangChain解析PDF文件示例,双栏PDF可解析。如果pdf含有图片,需要安装`rapidocr-onnxruntime`。
@Prerequisite for use:pip install pypdf,pip install rapidocr-onnxruntime
@Note:不支持GPU加速。
@Reference link:https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#extracting-images
"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("example_data/LayoutParser_基于深度学习的文档图像分析的统一工具包.pdf", extract_images=True)
pages = loader.load()
print(pages[3].page_content)    # The page index starts counting from 0.