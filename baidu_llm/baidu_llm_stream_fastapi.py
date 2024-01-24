"""
@author:ChenPeilong(peilongchencc@163.com)
@description:结合百度官方流式输出示例,实现基于fastapi和aiohttp的异步调用。
"""
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import StreamingResponse
import aiohttp
import json
import os
import time
from loguru import logger
from dotenv import load_dotenv

app = FastAPI()

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置日志
logger.remove()
logger.add("baidu_llm.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

# 从环境变量中读取 API Key 和 Secret Key
API_KEY = os.getenv("BAIDU_API_KEY")
SECRET_KEY = os.getenv("BAIDU_SECRET_KEY")

# 初始化访问令牌和令牌过期时间
ACCESS_TOKEN = ""
EXPIRES_IN = 0  # token的有效期（秒）

async def fetch_token():
    global ACCESS_TOKEN, EXPIRES_IN
    try:
        token_url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}"

        async with aiohttp.ClientSession() as session:  # 创建会话
            async with session.get(token_url) as response:  # 发送GET请求
                response.raise_for_status()  # 确保请求成功
                result = await response.json()  # 解析响应为JSON
                logger.info("成功获取访问令牌")
                ACCESS_TOKEN = result["access_token"]  # 访问令牌
                EXPIRES_IN = int(result["expires_in"]) + int(time.time())      # 令牌过期时间
    except Exception as e:
        logger.error(f"获取访问令牌失败：{e}")
        raise

async def get_access_token():
    global ACCESS_TOKEN, EXPIRES_IN
    # 如果token为空或者已过期，重新获取
    if not ACCESS_TOKEN or time.time() > EXPIRES_IN:
        await fetch_token()
    return ACCESS_TOKEN


async def call_chat_api(access_token, user_history):
    try:
        CHAT_API_URL = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token={access_token}"
        headers = {"Content-Type": "application/json"}
        data = {
            "messages": user_history,
            "stream": True
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(CHAT_API_URL, headers=headers, json=data) as response:
                response.raise_for_status()
                logger.info("聊天API调用成功")
                # async for line in response.content.iter_any():  # 选择使用这种方式每次获取的片段不一
                async for line in response.content:               # 选择使用这种方式每次只获取一个片段
                    yield line  # 逐行yield
    except Exception as e:
        logger.error(f"调用聊天API失败：{e}")
        raise

@app.post("/chat")
async def chat(user_input: str = Form(...), chat_history: str = Form(...)):
    try:
        # 每次请求前获取有效的token
        access_token = await get_access_token()  # 获取访问令牌
        if not user_input:
            logger.warning("用户输入为空")
            raise ValueError("用户输入为空")

        # 因为传入的是json数据，需要解码
        chat_history = json.loads(chat_history)
        logger.info(f"当前对话历史为:\n{chat_history}\n 数据类型为:{type(chat_history)}")

        user_history = []   # 存储用户聊天信息
        # 如果历史聊天数据不为空
        if chat_history:
            for user_message, bot_message in chat_history:
                user_history.append({"role": "user", "content": user_message})
                user_history.append({"role": "assistant", "content": bot_message})
        # 前一步构成的user_history是偶数，这里需要加上当前输入，构成奇数的content
        user_history.append({"role": "user", "content": user_input})

        # 调用聊天API
        chat_response = call_chat_api(access_token, user_history)  # 无需await，因为StreamingResponse会处理异步迭代器
        return StreamingResponse(chat_response, media_type="text/event-stream")  # 使用StreamingResponse返回
    except ValueError as ve:
        logger.error(f"无效输入：{ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"处理聊天请求时发生错误：{e}")
        raise HTTPException(status_code=500, detail="内部服务器错误")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8848)