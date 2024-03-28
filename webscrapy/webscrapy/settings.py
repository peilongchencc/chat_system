# Scrapy settings for webscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "webscrapy"

SPIDER_MODULES = ["webscrapy.spiders"]
NEWSPIDER_MODULE = "webscrapy.spiders"

# 日志文件配置
# scrapy默认日志路径
LOG_FILE = 'scrapy_log_default.txt'
# 自定义日志文件的路径
CUSTOM_LOG_FILE = 'scrapy_log_custom.txt'
# 日志级别配置
LOG_LEVEL = 'DEBUG'  # scrapy默认将DEBUG级别日志输出到终端，可以自己根据需要调整为INFO, WARNING等
# 终端是否输出日志，False为输出，True为不输出。
LOG_STDOUT = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 负责任地爬取数据，通过在用户代理上标识自己（以及你的网站）。
#USER_AGENT = "webscrapy (+http://www.yourdomain.com)"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

# Obey robots.txt rules
# 遵守 robots.txt 规则，默认是 `ROBOTSTXT_OBEY = True`，爬取一些反爬网站时，需要注释掉。
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 默认情况下，Scrapy会启用Cookies（即COOKIES_ENABLED的默认值是True），这意味着Scrapy会自动处理网站发送的Cookies，并在后续的请求中发送这些Cookies。
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}
# DEFAULT_REQUEST_HEADERS = {
#     'Cookie': 'BAIDUID=FC940DAC3FB27BDA14F94D67E7C7FE70:FG=1; BAIDUID_BFESS=FC940DAC3FB27BDA14F94D67E7C7FE70:FG=1; BIDUPSID=FC940DAC3FB27BDA14F94D67E7C7FE70; PSTM=1710294800; delPer=0; BDRCVFR[w2jhEs_Zudc]=mbxnW11j9Dfmh7GuZR8mvqV; PSINO=2; ariaDefaultTheme=undefined; ZFY=Mk:BPnX94wrgt4ZpWGXM0EJXyo9:BnLhyqg409L66JWu0:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; BCLID=11377979125998928077; BCLID_BFESS=11377979125998928077; BDSFRCVID=MzFOJexroG3h5Gvqnderuzt4m9VHYS6TDYLEOwXPsp3LGJLVYKuFEG0Ptsi54LI-ox_vogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=MzFOJexroG3h5Gvqnderuzt4m9VHYS6TDYLEOwXPsp3LGJLVYKuFEG0Ptsi54LI-ox_vogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI-5tIvDqTrP-trf5DCShUFsWRTlB2Q-XPoO3KOsMq3CKtTfbJD02l8J26cpWN5g_fbgylRp8P3y0bb2DUA1y4vpXxnt3eTxoUJ2-bIhMhRVqtnWBnKebPRiJPr9QgbPBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMD5oL3e; H_BDCLCKID_SF_BFESS=tRk8oI-5tIvDqTrP-trf5DCShUFsWRTlB2Q-XPoO3KOsMq3CKtTfbJD02l8J26cpWN5g_fbgylRp8P3y0bb2DUA1y4vpXxnt3eTxoUJ2-bIhMhRVqtnWBnKebPRiJPr9QgbPBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMD5oL3e; H_PS_PSSID=40010_40170_39662_40207_40211_40217_40080_40365_40352_40303_40368_40401_40415_40465_40461; BAIDU_WISE_UID=wapp_1710840298677_904; arialoadData=false; RT="z=1&dm=baidu.com&si=112a6888-4f87-4f8a-a543-7c784f04e5a0&ss=lty652ls&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=58c1xgo2&cl=x48&ul=14mz&hd=14nv"; ab_sr=1.0.1_ZjhkMDBkNDJjNjExYWUwN2QyNTg0YmUxNDZiMDBhOWJhZjNhZjQ5YTk1ZTI4YTMxOGIzOTBlMWUwMzAyNWJlMTkzYTllNWFiNzMwZmIzYmM0MmU1Njg5YzNlNGQ5MGY1NThkYmE5N2Q1YjUzYjhlMTI5Mjk4N2RkNWI3ODRlZDhkZDFiYzU2ZmRkOTg3NzA3YzBhZTQyZTk2ZmNjMmY0Ng==',
#     # 添加其他需要的请求头...
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "webscrapy.middlewares.WebscrapySpiderMiddleware": 543,
#}

# 添加Splash专用的去重过滤器和一个新的DUPEFILTER_CLASS：
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "webscrapy.middlewares.WebscrapyDownloaderMiddleware": 543,
#}
# 设置scrapy-splash中间件
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "webscrapy.pipelines.WebscrapyPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# 启用自动限速
AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
AUTOTHROTTLE_START_DELAY = 1
# 最大下载延迟，防止延迟过长
AUTOTHROTTLE_MAX_DELAY = 2
# 启用显示自动限速的调试信息
AUTOTHROTTLE_DEBUG = True

# 插件scrapy-splash相关设置
SPLASH_URL = 'http://localhost:8050'


# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
