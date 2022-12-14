
#from pymongo import MongoClient
import pymongo
#################################################################

# Team 1

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

#client = MongoClient("mongodb://127.0.0.1:27018/")

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27018/")

mydb = myclient["projet-mongo"]

mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)


print(mydb)

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "projet-mongo" in dblist:
  print("The database exists.")