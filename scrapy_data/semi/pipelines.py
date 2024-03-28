# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os
from itemadapter import ItemAdapter


class SemiPipeline:
    def process_item(self, item, spider):
        return item

class JsonExportPipeline:
    """Json文件输出逻辑
    """
    def __init__(self, files_store):
        self.files_store = files_store

    @classmethod
    def from_crawler(cls, crawler):
        # 从 settings.py 获取 "文件保存路径" 的值
        return cls(
            files_store=crawler.settings.get('OUTPUT_DIR_OF_ZHXW')
        )

    def open_spider(self, spider):
        # 爬虫启动时执行，检查是否创建目录
        if not os.path.exists(self.files_store):
            os.makedirs(self.files_store)

    def clean_item(self, item):
        """清理项目中的特殊字符，例如 '\n', '\u2002'
        """
        if isinstance(item, dict):
            for key, value in item.items():
                item[key] = self.clean_item(value)
        elif isinstance(item, list):
            return [self.clean_item(elem) for elem in item]
        elif isinstance(item, str):
            # 替换掉字符串中的特殊字符，例如换行符和不间断空格
            return item.replace('\n', ' ').replace('\u2002', ' ').strip()
        return item

    def process_item(self, item, spider):
        # 首先清理项目中的特殊字符
        cleaned_item = self.clean_item(item)

        # 定义文件名，这里使用文章标题作为文件名，确保文件名对于文件系统是安全的
        # 替换文件名中的特殊字符，避免 "/" 等特殊字符造成目录分级。
        filename = f"{cleaned_item['metadata']['title']}".replace('/', '_').replace(':', '_')
        # 为文件名添加时间标签，避免覆盖写入
        # 例如网站有重复的文章标题 "半导体所召开党委理论学习中心组学习（扩大）会"，但文章时间不同
        filename = filename + f"{cleaned_item['metadata']['date']}.json".replace('-', '_')
        file_path = os.path.join(self.files_store, filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(cleaned_item, file, ensure_ascii=False, indent=4)

        return item

    def close_spider(self, spider):
        # 爬虫关闭时执行，暂时只作为占位。
        pass
