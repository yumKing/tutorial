import scrapy


class QuotesSpider(scrapy.Spider):
    """docstring for QuotesSpider"""
    # def __init__(self, arg):
    # 	super(QuotesSpider, self).__init__()
    # 	self.arg = arg

    name = 'quotes'

    # def start_requests(self):
    start_urls = [
        'http://quotes.toscrape.com/page/1',
        # 'http://quotes.toscrape.com/page/2',
    ]
    # for url in start_urls:
    #     yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('saved file %s' % filename)
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
