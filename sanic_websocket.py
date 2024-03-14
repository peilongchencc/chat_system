from sanic import Sanic
from sanic.response import html
from sanic.websocket import WebSocketProtocol

app = Sanic("websocket_example")

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = '服务器时间: {}'.format(datetime.now().isoformat())
        print('发送: ' + data)
        await ws.send(data)
        await asyncio.sleep(1)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, protocol=WebSocketProtocol)