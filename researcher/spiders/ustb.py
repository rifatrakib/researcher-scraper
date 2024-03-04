import scrapy


class UstbSpider(scrapy.Spider):
    name = "ustb"
    allowed_domains = ["enscce.ustb.edu.cn"]
    start_urls = ["https://enscce.ustb.edu.cn/Teach/TeacherList/"]

    def parse(self, response):
        print(f"{response.status = }")
