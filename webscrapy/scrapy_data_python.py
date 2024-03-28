from scrapy.crawler import CrawlerProcess
from scrapy import signals
from scrapy.signalmanager import dispatcher
from webscrapy.spiders.webscrapy import WebScrapySpider  # 从WebScrapy项目导入自己的Spider
from scrapy.utils.project import get_project_settings

def run_spider(urls):
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())

    # process.crawl(WebScrapySpider, start_urls=urls)
    process.crawl(WebScrapySpider, urls=','.join(urls))
    process.start()

    return results

if __name__ == "__main__":
    urls = ['https://baijiahao.baidu.com/s?id=1793832549445442560']
    # urls = ["https://quotes.toscrape.com/tag/humor/"]
    scraped_data = run_spider(urls)
    print(scraped_data)