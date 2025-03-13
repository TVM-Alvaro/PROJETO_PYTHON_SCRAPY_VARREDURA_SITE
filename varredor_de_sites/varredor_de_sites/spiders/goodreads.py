import scrapy

# CamelCase


class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade
    name = 'quotebot'
    # Request

    def start_requests(self):
        # Definir url(s) a varrer
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response

    def parse(self, response):
        # aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quote']"):
            yield {
                'frase': elemento.xpath(".//div[@class='quoteText']/text()").get().strip(),
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get().strip(),
                # para achar as tags foi usado um xpath composto.
                'tags': elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall()
            }