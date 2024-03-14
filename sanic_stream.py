from sanic import Sanic
from sanic.response import stream

app = Sanic("StreamingExample")

@app.post("/stream")
async def stream_handler(request):
    async def streaming_response(response):
        # 假设客户端以流的形式发送数据
        async for data in request.stream:
            # 对于每一块接收到的数据，我们可以进行处理，这里简单地原样返回
            # 注意：实际应用中可能需要根据业务逻辑对数据进行处理
            await response.write(data)

    # 返回一个流式响应，调用上面定义的异步生成器
    return stream(streaming_response, content_type="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
