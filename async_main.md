

我使用以下代码获取access_info的信息，但access_info中不含有过期时间，对方只告诉我access_token过期时间是2小时，我应该如何自己添加过期时间呢，当access_token没有过期时，不再获取access_token。

请使用time库构建过期时间处理逻辑，在`fetch_access_info_async`函数的返回值中添加获取access_token的时间戳，过期时间请写在`get_llm_response`函数中，过期时间定义为1小时55分钟。

注意：请使用redis。

```python
import time
from tongyi_chatbot.con_ali_access_token_interface import fetch_access_info_async

async def get_llm_response(context, user_input):
    access_token, channel_id, stream_secret = await fetch_access_info_async()
    # 其他代码省略
```

```python
async def fetch_access_info_async():
    """fetch access information for Alibaba Chatbot using access_key and access_key_secret asynchronously.
    """
    access_key, access_key_secret, agent_key = load_environment_variables()
    client = create_client(access_key, access_key_secret)
    apply_for_stream_access_token_request = chatbot_20220408_models.ApplyForStreamAccessTokenRequest(agent_key=agent_key)
    runtime = util_models.RuntimeOptions()
    try:
        access_info = await client.apply_for_stream_access_token_with_options_async(apply_for_stream_access_token_request, runtime)
        # print(f"\Login information:\n{access_info}")
        # print(f"\nACCESS_TOKEN is:\n{access_info.body.access_token}")
        return (access_info.body.access_token,
                access_info.body.channel_id,
                access_info.body.stream_secret)
    except Exception as error:
        # 错误 message
        print(error.message)
        # 诊断地址
        print(error.data.get("Recommend"))
        UtilClient.assert_as_string(error.message)
```


http://8.140.203.136:7860

我的 ubuntu 服务器只有终端界面，没有图形界面。但对方给我发的客户端必须要有图形界面才能操作，我该怎么办呢？

http_proxy=http://127.0.0.1:8118
https_proxy=http://127.0.0.1:8118


我使用的ubuntu 18.04，我使用以下指令临时终端开启网络代理，我如何永久使用呢？

```txt
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```