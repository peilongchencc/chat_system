from sanic import Sanic

app = Sanic("ModelApp")

@app.post("/stream", stream=True)
async def handler(request):
    response = await request.respond(content_type="text/event-stream")
    async def streaming(response):
        while True:
            body = await request.stream.read()
            if body is None:
                break
            body = body.decode("utf-8") + "##"
            await response.send(f"data:{body}\n\n")   # 标准sse响应需要的格式，适用于postman测试

    return streaming(response)  # 这里是否要换为await

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    
This GPT has been moved to Keymate.AI Search GPT Please use it instead!