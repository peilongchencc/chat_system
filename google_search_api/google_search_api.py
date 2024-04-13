import os
import requests
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")

def google_search(query):
    GOOGLE_SEARCH_API_KEY=os.getenv("GOOGLE_SEARCH_API_KEY")
    GOOGLE_SEARCH_CX=os.getenv("GOOGLE_SEARCH_CX")
    url = f'https://www.googleapis.com/customsearch/v1?key={GOOGLE_SEARCH_API_KEY}&cx={GOOGLE_SEARCH_CX}&q={query}'

    response = requests.get(url)
    result = response.json()

    return result

# 使用示例
results = google_search('OpenAI')
for item in results['items']:
    print(item['title'], item['link'])