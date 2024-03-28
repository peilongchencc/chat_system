import scrapy
from datetime import datetime, timedelta
# 导入自定义的日志配置
from ..log_config import setup_logging

# 初始化日志配置并获取logger实例
logger = setup_logging()

class MySpider(scrapy.Spider):
    name = 'semi'
    allowed_domains = ['semi.cas.cn']

    def __init__(self, start_urls=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        if start_urls is not None:
            self.start_urls = start_urls.split(',')  # 从逗号分隔的字符串转换为列表
        else:
            logger.info(f"缺少参数:start_urls")
            # self.start_urls = ['https://semi.cas.cn/xwdt/zhxw/']  # 默认URL

    def parse(self, response):
        article_title = response.xpath('//title/text()').get()  # 使用XPath或CSS选择器提取标题
        article_content = response.xpath('//body//text()').getall()  # 提取正文内容
        yield item
        # 确定过去3年的日期范围
        date_limit = datetime.now() - timedelta(days=3*365)  # 简单方法，未考虑闰年
        # 用于标记是否找到在日期限制内的文章
        found_recent_article = False
        
        # 取包含有特定class="fw_t"的<td>元素，遍历每个条目
        for item in response.xpath('//td[@class="fw_t"]/..'):
            
            date_field = item.xpath('./td[@class="fw_s"]/text()')
            # logger.info(f"提取出的时间字段为：{date_field}")
            
            # 提取并处理时间信息
            date_str = date_field.extract_first().strip()
            logger.info(f"处理后的时间字段为：{date_str}")
            
            # 将字符串日期转换为datetime对象
            article_date = datetime.strptime('20' + date_str, '%Y-%m-%d')

            # 根据文章日期处理数据
            if article_date >= date_limit:
                # 标记当前文章符合日期范围
                found_recent_article = True
                
                # 提取相对路径并转换为完整URL
                relative_url = item.xpath('./td[@class="fw_t"]/a/@href').extract_first().strip()
                
                full_url = response.urljoin(relative_url)
                
                # 对每个文章URL发起请求，并将响应传递给parse_article方法处理
                request = scrapy.Request(full_url, callback=self.parse_article)
                request.meta['date'] = article_date.strftime('%Y-%m-%d')  # 传递文章日期
                request.meta['url'] = full_url  # 传递文章URL
                
                yield request

        # 如果在当前页面找到至少一篇符合条件的文章，则继续翻页。否则不再翻页，结束爬取。
        if found_recent_article:
            next_pages = response.css('div.t_page a::attr(href)').extract()
            for page_url in next_pages:
                full_page_url = response.urljoin(page_url.strip())
                # logger.info(f"下一页的url为：{full_page_url}")
                yield scrapy.Request(full_page_url, callback=self.parse)

    def parse_article(self, response):
        article_date = response.meta['date']
        article_url = response.meta['url']

        # 由于文章的属性可能为 "trs_editor"、"trs_editor_view"、"Trs_editor"、"TRS_Editor"等多种情况
        # 需要以不区分大小写的方式，提取文章内容
        article_content = " ".join(response.xpath(
            '//div[contains(translate(@class, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "trs_editor")]//*[not(self::style) and not(self::script)]//text()'
            ).extract()).strip()

        # 由于网页结构不统一，采用模糊匹配检索
        article_field = response.css('.title ::text').get()
        article_title = article_field.strip()

        # 提取文章目录
        breadcrumbs = response.xpath('//div[@class="Position"]/span/a/text()').extract()
        # 将目录列表转换为字符串，并用" > "连接
        breadcrumbs_str = ' > '.join(breadcrumbs)
        # 将目录添加到标题中
        full_title = f"{breadcrumbs_str}: {article_title}"
        # 构造要保存的数据
        yield {
            "page_content": article_content,
            "metadata": {
                "source": article_url, 
                "title": full_title,  # 使用包含目录的完整标题
                "date": article_date
            }
        }