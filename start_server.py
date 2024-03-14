from sanic import Sanic, response
from classifier import Classify_data  # 假设这是你的模型类

app = Sanic("ModelApp")

# 在启动应用时加载模型
@app.listener('before_server_start')
async def load_model(app, loop):
    app.ctx.classify_model = Classify_data()

@app.route('/reload_model', methods=['GET'])
async def reload_model(request):
    # 重新加载模型
    app.ctx.classify_model = Classify_data()
    return response.json({"status": "Model reloaded successfully"})

# 使用已加载的模型进行预测
@app.route('/classify', methods=['POST'])
async def classify(request):
    # 获取请求数据
    data = request.json
    # 直接使用已加载的模型进行预测
    prediction = app.ctx.classify_model.predict(data)
    return json({"prediction": prediction})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)