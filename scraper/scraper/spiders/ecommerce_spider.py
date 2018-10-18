import scrapy
from scraper.items import Product


class ecommSpider(scrapy.Spider):
    name = "ecommerce"


    def start_requests(self):
        urls = [
            'https://www.appliancesdelivered.ie',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        navlinks =  response.css("body div.container header nav ul li a::attr(href)").extract()
        for link in navlinks[0:8]:
            url = 'https://www.appliancesdelivered.ie'+link
            print("parsing: "+url)
            yield scrapy.Request(url=url, callback=self.parseList)


    def parseList(self, response):
        productLinks = response.css("div.search-results-product div.product-image a::attr(href)").extract()
        for plink in productLinks:
            print("parsing product: "+plink)
            yield scrapy.Request(url=plink, callback=self.parseProduct)


    def mapSpecs(self, l, n):
        outDict = {}
        for i in range(0, len(l), n):
            outDict[l[i:i + n][0]] = l[i:i + n][1]
        return outDict

    def parseProduct(self, response):
        item = Product()
        item['images'] = response.css("#product-gallery ol li img::attr(src)").extract()
        item['header'] = response.css("#product-title::text").extract()[0]
        item['model'] = response.css("#product-title::text").extract()[0].split(" ")[-1]
        item['global_category'] = response.css("ul.breadcrumb li a::text").extract_first()
        item['category'] = response.css("ul.breadcrumb li a::text").extract()[1]
        item['brand'] = response.css("img.article-brand::attr(alt)").extract()[0]
        item['description'] = response.css("#product-lg-overview p::text").extract_first()
        item['specs'] = self.mapSpecs(response.css("#product-lg-overview table tr td::text").extract(),2)
        yield item

