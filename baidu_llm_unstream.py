"""
@author:ChenPeilong(peilongchencc@163.com)
@description:结合百度官方多轮对话(非流式输出)示例所写。
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
                "content": "请介绍一下你自己"
            },
            {
                "role": "assistant",
                "content": "我是百度公司开发的人工智能语言模型，我的中文名是文心一言，可以协助您完成范围广泛的任务并提供有关各种主题的信息，比如回答问题，提供定义和解释及建议。如果您有任何问题，请随时向我提问。"
            },
            {
                "role": "user",
                "content": "我在上海，周末可以去哪里玩？"
            },
            {
                "role": "assistant",
                "content": "上海是一个充满活力和文化氛围的城市，有很多适合周末游玩的地方。以下是几个值得推荐的地方：\n\n1. 上海科技馆：上海科技馆是中国大陆最大的科技馆之一，有许多互动展览和科学实验室，可以让您了解科技的发展历史和最新成果。\n2. 上海博物馆：上海博物馆是一座集艺术、历史和文化于一体的博物馆，有许多精美的艺术品和文物，可以让您深入了解中国和世界的文化历史。\n3. 外滩：外滩是上海的标志性景点之一，有许多高楼大厦和繁华的商业街区，是欣赏黄浦江美景和城市风貌的好去处。\n4. 上海迪士尼乐园：上海迪士尼乐园是世界上最大的迪士尼主题公园之一，有许多精彩的游乐项目和演出，可以让您尽情享受娱乐和欢乐。\n5. 上海野生动物园：上海野生动物园是一个以自然保护为主题的野生动物园，有许多珍稀动物和植物，可以让您近距离接触大自然。\n\n这些地方都是上海周末游玩的好去处，可以根据自己的兴趣和需求选择合适的行程。"
            },
            {
                "role": "user",
                "content": "上海有哪些美食？"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    
if __name__ == '__main__':
    main()

