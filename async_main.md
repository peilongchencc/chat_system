






http://8.140.203.136:7860

我的 ubuntu 服务器只有终端界面，没有图形界面。但对方给我发的客户端必须要有图形界面才能操作，我该怎么办呢？

http_proxy=http://127.0.0.1:8118
https_proxy=http://127.0.0.1:8118


我使用的ubuntu 18.04，我使用以下指令临时终端开启网络代理，我如何永久使用呢？

```txt
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```