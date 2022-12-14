
from pymongo import MongoClient

#################################################################

# Team 1


# import scrapy

# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     start_urls = ['https://www.cybertek.fr']

#     def parse(self, response):
#         for title in response.css('.oxy-post-title'):
#             yield {'title': title.css('::text').get()}

#         for next_page in response.css('a.next'):
#             yield response.follow(next_page, self.parse)




#################################################################


data = [{
    'url_image' : "https://www.cybertek.fr/images_produits/e0f01a81-4966-4612-ac8a-d75da145a79a.jpg",
    'modele' : "MSI bim",
    'prix' : 1200,
    'utilisation' : "bureautique",
    'resolution' : "4k",
    'ram' : 8,
    'constructeurGPU' : "Intel",
    'tailleEcran' : 15,
    'processeur' : "i5",
    'tailleSD' : 256,
    'chipSet' : "GF RTX"
},{
    'url_image' : "https://www.cybertek.fr/images_produits/e0f01a81-4966-4612-ac8a-d75da145a79a.jpg",
    'modele' : "MSI bim 2",
    'prix' : 700,
    'utilisation' : "bureautique",
    'resolution' : "4k",
    'ram' : 8,
    'constructeurGPU' : "Intel",
    'tailleEcran' : 13,
    'processeur' : "i5",
    'tailleSD' : 512,
    'chipSet' : "GF RTX"
}]

# print(data)

# database connection
client = MongoClient("mongodb://127.0.0.1:27018/")

mydb = client["scrapy-database"]

# get collection
db_collection = mydb['computers']

# insert new computers inside tthe collection
inserted = db_collection.insert_many(data)

# print the result
print(str(len(inserted.inserted_ids)) + " documents inserted")

