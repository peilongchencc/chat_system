# chat_system

Implementing a dialogue system through interfaces(通过接口实现对话系统)。<br>

> gradio部分只能说勉强能用，还有很多需要优化的地方，但不影响正常功能使用。

- [chat\_system](#chat_system)
  - [本地运行:](#本地运行)
  - [依赖项安装:](#依赖项安装)
    - [使用`pip`指令进行一键安装:](#使用pip指令进行一键安装)
    - [逐个安装依赖项:](#逐个安装依赖项)

## 本地运行:

以fastapi异步调用baidu的API进行流式输出为例:<br>

1.参考`.env.local`文件，将`BAIDU_API_KEY`、`BAIDU_SECRET_KEY`修改为自己的KEY。

> 笔者使用的是官方给的免费额度，额度较低，建议改为自己的KEY。

2.运行fastapi模块:<br>

```bash
python baidu_llm_stream_fastapi
```

3.运行gradio交互界面:<br>

```bash
gradio gradio_stream_generator.py
```

4.网页打开`http://127.0.0.1:7860/`，效果如下:

![image](./materials/gradio界面.jpg)


## 依赖项安装:

### 使用`pip`指令进行一键安装:

```bash
pip install -r requirements.txt
```

### 逐个安装依赖项:

终端切换到自己的虚拟环境，然后依次运行下列指令即可:<br>

> 笔者使用的是`python==3.10.11`，python版本推测3.8+即可。

```bash
pip install aiohttp
pip install fastapi
pip install uvicorn
pip install gradio
pip install loguru
pip install python-dotenv
```