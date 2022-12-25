from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pymongo import MongoClient

class CrawlingSpider(CrawlSpider):
    name = "mainCrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    #PROXY_SERVER ="IP ADDRESS"

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue",deny="category"),callback="parse_item")
    )

    def parse_item(self, response):
        livre = {
            "title" : response.css(".product_main h1::text").get(),
            "price": response.css("div.product_main p.price_color::text").get().replace("\u00a3",""),
            "availability": response.css(".availability::text")[1].get().replace("\n","").replace("  ",""),
            "picture": response.css("div.item img::attr(src)").get().replace("../..","https://books.toscrape.com"),
            "description":response.css("article.product_page p::text")[10].get()
        }
        # database connection
        client = MongoClient("mongodb://127.0.0.1:27018/")
        mydb = client["scrapy-database"]
        # get collection
        db_collection = mydb['livres']
        # key = {'title': livre.title}
        key = {'title':livre["title"]}
        inserted = db_collection.update_one(key, {"$set": livre}, upsert=True)

        
    