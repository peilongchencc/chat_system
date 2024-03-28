# semi
- [semi](#semi)
  - [项目概述:](#项目概述)
  - [项目依赖项安装:](#项目依赖项安装)
  - [settings.py 配置(可选项):](#settingspy-配置可选项)
  - [项目运行方式:](#项目运行方式)
  - [备注:](#备注)


## 项目概述:

在域名为 `'semi.cas.cn'` 的基础上，爬取 `'https://semi.cas.cn/xwdt/zhxw/'` 中过往3年的文章，并按照以下格式进行存储。<br>

```json
{
    "page_content": "5 月 22 日上午，半导体...",
    "metadata": {
        "source": "https://semi.cas.cn/xwdt/zhxw/202105/t20210522_6036445.html",
        "title": "首页 > 新闻动态 > 综合新闻: “揭开半导体世界的神秘面纱”——中国科学院半导体研究所举办2021年公众科学日活动",
        "date": "2021-05-22"
    }
}
```

每篇文章为一个json文件，文件名命名方式为 **目录+title+date**，例如 `首页 > 新闻动态 > 综合新闻_ “揭开半导体世界的神秘面纱”——中国科学院半导体研究所举办2021年公众科学日活动2021_05_22.json`。<br>

## 项目依赖项安装:

笔者使用的python版本为 `python==3.10.11`，项目中除了scrapy，使用的都是python标准库，不需要额外安装。<br>

笔者安装的Scrapy版本`scrapy==2.11.0`，具体安装方式可参考以下内容:<br>

conda安装方式:<br>

```bash
conda install -c conda-forge scrapy
```

pip安装方式:<br>

```bash
pip install Scrapy
```

## settings.py 配置(可选项):

项目中的配置参数已全部放入 `settings.py` 文件，例如爬取时的请求延迟，json文件的保存路径等。<br>

可根据自定义需求进行修改，如果不清楚scrapy配置，不需要更改 `settings.py` 文件，笔者已全部配置好。<br>

## 项目运行方式:

scrapy安装完成后，`cd` 到 `scrapy.cfg` 同级目录，然后终端运行以下指令，即可开始爬取数据:<br>

```bash
scrapy crawl semi
```

指令运行后，json文件会输出到 `zhxw` (综合新闻) 文件夹下。同时会在 `scrapy.cfg` 同级目录下创建 `scrapy_log_custom.txt`、`scrapy_log_default.txt`文件。<br>

- `scrapy_log_custom.txt`: 记录自定义log信息。

- `scrapy_log_default.txt`: 记录scrapy默认信息。


## 备注:

爬取到的文件中，部分数据 "page_content" 为空并不是报错，是因为网页中内容是图片，没有文本可以爬取。示例如下：<br>

```txt
{
    "page_content": "",
    "metadata": {
        "source": "https://semi.cas.cn/xwdt/zhxw/202212/t20221231_6592363.html",
        "title": "首页 > 新闻动态 > 综合新闻: 新年致辞",
        "date": "2022-12-31"
    }
}
```

笔者使用的系统为 ubuntu 18.04，未测试 windows、macos 中代码运行效果。<br>