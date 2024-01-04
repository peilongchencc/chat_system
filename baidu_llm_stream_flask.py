"""
@author:ChenPeilong(peilongchencc@163.com)
@description:结合百度官方流式输出示例,实现基于flask的同步调用。
"""
from flask import Flask, request, Response, stream_with_context
import requests
import json
import os
from loguru import logger
from dotenv import load_dotenv

app = Flask(__name__)

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置终端控制台不输出日志
logger.remove()
# 使用loguru设置日志写入,包括格式、轮转等
logger.add("baidu_llm.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

# 从环境变量中读取API Key和Secret Key
API_KEY = os.getenv("BAIDU_API_KEY")  # 填入平台申请的实际APIKey
SECRET_KEY = os.getenv("BAIDU_SECRET_KEY")  # 填入平台申请的实际SecretKey

# 获取access_token的函数
def get_access_token():
    # 定义获取access_token的URL
    token_url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}"
    try:
        response = requests.get(token_url)
        response.raise_for_status()
        return response.json()["access_token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"获取access_token失败: {e}")
        return None

# 获取access_token
ACCESS_TOKEN = get_access_token()

# 定义ERNIE-Bot聊天接口地址
CHAT_API_URL = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={ACCESS_TOKEN}"
user_chat_histories = {}  # 用于存储不同用户的聊天历史

@app.route('/chat', methods=['POST'])
def chat_with_ernie_bot():
    user_id = request.form.get('user_id')
    user_input = request.form.get('user_input')
    # 表单数据传入的是字符串，第一次开启会话传入的是None
    chat_history = request.form.get('chat_history')
    # 因为传入的是json数据，需要解码
    chat_history = json.loads(chat_history)
    print(f"当前对话历史为:\n{chat_history}\n 数据类型为:{type(chat_history)}")

    if not user_id:
        raise ValueError("缺少用户ID")
    if not user_input:
        raise ValueError("用户输入为空")

    user_history = user_chat_histories.get(user_id, [])
    # 如果历史聊天数据不为空
    if chat_history:
        for user_message, bot_message in chat_history:
            user_history.append({"role": "user", "content": user_message})
            user_history.append({"role": "assistant", "content": bot_message})
    # 前一步构成的user_history是偶数，这里需要加上当前输入，构成奇数的content
    user_history.append({"role": "user", "content": user_input})
    user_chat_histories[user_id] = []  # 更新用户的聊天历史

    headers = {"Content-Type": "application/json"}
    data = {
        "messages": user_history,
        "stream": True
    }

    response = requests.post(CHAT_API_URL, headers=headers, json=data, stream=True)
    response.raise_for_status()
    
    def generate():
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # 过滤掉保持连接的新行符
                yield chunk # 直接发送二进制数据

    return Response(stream_with_context(generate()), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(port=8848)
