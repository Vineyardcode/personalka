import scrapy

class PersonalkaSpiderSpider(scrapy.Spider):
    name = "personalka_spider"
    allowed_domains = ["personalka.cz"]
    start_urls = ["https://personalka.cz/pozice"]

    def parse(self, response):
        job_data = {}

        for branch in response.css('div.bg-white'):
            branch_name = branch.css('h3.text-2xl a.text-grey-darkest::text').get()
            if branch_name:
                branch_name = branch_name.strip()
                positions = branch.css('ul.list-reset li a::text').getall()
                job_data[branch_name] = positions

        yield job_data
