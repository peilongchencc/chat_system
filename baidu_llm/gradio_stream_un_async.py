"""
@author:ChenPeilong(peilongchencc@163.com)
@description:实现gradio交互界面,以非异步方式让gradio接收给定API的流式输出。
"""
import json
import requests
import gradio as gr

def predict(message, history):
    
    chat_history = json.dumps(history)  # history的数据类型为列表嵌套列表
    # 设置llm服务接口
    URL = 'http://localhost:8848/chat'
    # 设置传给llm服务接口的参数
    DATA = {
        'user_id': 'peilongchencc',
        'user_input': message,
        'chat_history': chat_history
    }

    llm_response = requests.post(URL, data=DATA, stream=True)    # 通过接口获取数据,得到的结果为一个生成器
    
    generated = ""  # 用于存储之前生成的字符
    for chunk_data in llm_response.iter_lines():
        # 防止出现 b'' 引起报错
        if chunk_data:
            decoded_line = chunk_data.decode('utf-8') # 将json数据转为可读形式
            data_dict = json.loads(decoded_line.replace('data: ', ''))  # 将JSON字符串转换为字典
            # 提取出需要的内容
            chunk_result = data_dict["result"]      # 当前为流式输出的某部分内容,需要拼接才能成为常规格式。
            generated += chunk_result                 # 将新字符添加到存储的字符串中
            yield generated

demo = gr.ChatInterface(
    predict,
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Ask me a question...", container=False, scale=7),
    title="Dragon Chatbot",
    description="Ask Dragon Chatbot any question",
    theme="soft",
    examples=["Hello", "请给我一份读取json文件的python代码", "\"consist\"的中文含义是什么？"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="删除上一轮对话",
    clear_btn="清空历史数据",
).queue()
demo.launch()