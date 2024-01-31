import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm_response = llm.invoke("how can langsmith help with testing?")

print(llm_response)     # content='你好！有什么我可以帮助你的吗？'
print(type(llm_response))   # <class 'langchain_core.messages.ai.AIMessage'>
print(llm_response.content) # 你好！有什么我可以帮助你的吗？