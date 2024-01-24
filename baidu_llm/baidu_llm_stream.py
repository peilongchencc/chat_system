"""
@author:ChenPeilong(peilongchencc@163.com)
@description:结合百度官方流式输出示例所写。
"""
import os
import requests
import json
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 从环境变量中读取API Key和Secret Key
API_KEY = os.getenv("BAIDU_API_KEY")  # 填入平台申请的实际APIKey
SECRET_KEY = os.getenv("BAIDU_SECRET_KEY")  # 填入平台申请的实际SecretKey


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}"
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你是谁"
            }
        ],
         "stream": True
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, stream=True)
    
    count_num = 0
    for line in response.iter_lines():
        if line:
            count_num += 1
            print(f"流式输出第{count_num}次的返回结果:")
            decoded_line = line.decode('utf-8')  # 将json数据转为可读形式
            print(decoded_line)

if __name__ == '__main__':
    main()