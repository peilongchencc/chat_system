"""
@author:ChenPeilong(peilongchencc@163.com)
@description:LangChain解析PDF文件示例,双栏PDF可解析。如果pdf含有图片,需要安装`rapidocr-onnxruntime`。如果需要解析数学公式,需要使用类似Mathpix的方法。
@Prerequisite for use:pip install pypdf,pip install rapidocr-onnxruntime, 需要将`MATHPIX_API_KEY`添加到环境变量。
@Note:不支持GPU加速。
@Reference link:https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-mathpix
"""

from langchain_community.document_loaders import MathpixPDFLoader
loader = MathpixPDFLoader("example_data/LayoutParser_基于深度学习的文档图像分析的统一工具包.pdf")   # 官网的"example_data/layout-parser-paper.pdf"就是笔者当前使用的文件；
data = loader.load()
print(data) # 笔者没有测试，笔者没有注册Mathpix。