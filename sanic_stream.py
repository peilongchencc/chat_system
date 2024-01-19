from sanic import Sanic
from sanic.request import Request

app = Sanic("MyApp")

@app.route("/ans", methods=["POST"])
async def test(request: Request):
    user_input = request.form.get("user_input")
    response = await request.respond(content_type="text/csv")
    await response.send(user_input)
    await response.send("foo,")
    await response.send("bar")

    # Optionally, you can explicitly end the stream by calling:
    await response.eof()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8848)