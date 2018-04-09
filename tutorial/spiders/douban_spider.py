import scrapy


class DoubanSpider(scrapy.Spider):
    """docstring for  DoubanSpider"""

    # def __init__(self, arg):
    #	 super(DoubanSpider, self).__init__()
    #	 self.arg = arg

    name = 'douban'
    allow_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/tag/#/?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1",
    ]

    def parse(self, response):
        filename = response.url.split("&")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
