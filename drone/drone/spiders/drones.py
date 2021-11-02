import scrapy


class DronesSpider(scrapy.Spider):
    name = "drones"
    allowed_domains = ["https://www.jessops.com/drones"]
    start_urls = ["http://https://www.jessops.com/drones/"]

    def parse(self, response):
        products = response.css("div.details-pricing")
        for product in products:
            item = {
                "name": product.css("a::text").get(),
                "price": product.css("p.price.large::text").get(),
            }
            yield
        pass
