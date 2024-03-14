有人告诉我可以通过以下方式，避免模型重复加载。但我如果想要不停服务更新模型，应该怎么操作呢？

```python
from sanic import Sanic
from sanic.response import json
from your_model_file import Classify_data  # 假设这是你的模型类

app = Sanic("ModelApp")

# 在启动应用时加载模型
@app.listener('before_server_start')
async def load_model(app, loop):
    app.ctx.classify_model = Classify_data()

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
```