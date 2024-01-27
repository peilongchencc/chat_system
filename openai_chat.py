"""
@author:ChenPeilong(peilongchencc@163.com)
@description:openai流式输出示例
"""
import os
from loguru import logger
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置日志
logger.remove()
logger.add("openai_stream.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)