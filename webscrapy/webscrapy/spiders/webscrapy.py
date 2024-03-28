import scrapy
from webscrapy.items import WebscrapyItem
# 在Spider中，使用Splash的execute端点来请求网页。这可以通过构造一个带有splash键的Request实现。
from scrapy_splash import SplashRequest
# 导入自定义的日志配置
from ..log_config import setup_logging

# 初始化日志配置并获取logger实例
logger = setup_logging()

class WebScrapySpider(scrapy.Spider):
    name = 'webscrapy'
    
    def __init__(self, urls=None, *args, **kwargs):
        super(WebScrapySpider, self).__init__(*args, **kwargs)
        logger.info(f"传入的网页链接为:{urls}")
        self.start_urls = urls.split(',') if urls else []
        logger.info(f"待爬取的网页为:{self.start_urls}")

    def start_requests(self):
        for url in self.start_urls:
            # SplashRequest是用来代替标准的Request，args={'wait': 0.5}告诉Splash等待0.5秒以完成JavaScript的执行。你可以根据页面加载的实际情况调整等待时间。
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        logger.info(f"开始进行网页解析-->")
        item = WebscrapyItem()
        item['title'] = response.xpath('//title/text()').get()
        item['content'] = response.xpath('//body//text()').getall()
        logger.info(f"爬取到的文章标题为：{item['title']}")
        yield item