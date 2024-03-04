import scrapy


class UstbSpider(scrapy.Spider):
    name = "ustb"
    allowed_domains = ["enscce.ustb.edu.cn"]
    start_urls = ["https://enscce.ustb.edu.cn/Teach/TeacherList/"]

    def parse(self, response):
        sections = response.xpath("/html/body/div/div/div[2]/ul/li")

        for section in sections:
            for teacher in section.css("div.detailss > a"):
                yield scrapy.Request(
                    response.urljoin(teacher.attrib["href"]),
                    callback=self.parse_teacher,
                )

    def parse_teacher(self, response, **kwargs):
        teacher = {
            "name": response.css("div.details_t_left > div::text").get(),
            "title": response.css("dd:nth-child(2) > div.duty_right::text").get(),
            "department": response.css("dd:nth-child(1) > div.duty_right::text").get(),
            "mail": response.css("dd:nth-child(6) > div.duty_right::text").get(),
            "research_interests": response.css("dd:nth-child(3) > div.duty_right.duty_nows::text").get(),
        }
        print(teacher)
