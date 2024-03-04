import json
from pathlib import Path

from openpyxl import Workbook
from pydash import human_case
from scrapy import signals


class ResearcherPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.data = []

        self.json_file = Path(f"data/json/{spider.name}.json")
        self.json_file.parent.mkdir(parents=True, exist_ok=True)
        self.json_file.touch(exist_ok=True)

        self.excel_file = Path(f"data/excel/{spider.name}.xlsx")
        self.excel_file.parent.mkdir(parents=True, exist_ok=True)
        self.excel_file.touch(exist_ok=True)

    def spider_closed(self, spider):
        self.save_json(spider)
        self.save_excel(spider)

    def process_item(self, item, spider):
        self.data.append(item.model_dump())
        return item

    def save_json(self, spider):
        with open(self.json_file, "w") as writer:
            writer.write(json.dumps(self.data, indent=4))

    def save_excel(self, spider):
        wb = Workbook()
        ws = wb.active
        ws.append([human_case(header) for header in list(self.data[0].keys())])
        for item in self.data:
            ws.append(list(item.values()))
        wb.save(self.excel_file)
