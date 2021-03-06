import scrapy

from scrapytutorial.items import ScrapytutorialItem
class DmozSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains=["dmoz.org"]
	start_urls=["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]

	def parse(self,response):
	# pass
		# filename=response.url.split("/")[-2]
		# with open(filename,'wb') as f:
		# 	f.write(response.body)
		for sel in response.xpath('//ul/li'):
			# title=sel.xpath('a/text()').extract()
			# link=sel.xpath('a/@href').extract()
			# desc=sel.xpath('text()').extract()
			# print title, link, desc
			item=ScrapytutorialItem()
			item['title']=sel.xpath('a/text()').extract()
			item['link']=sel.xpath('a/@href').extract()
			item['desc']=sel.xpath('text()').extract()
			yield item