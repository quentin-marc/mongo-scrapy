from pymongo import MongoClient
import webbrowser

client = MongoClient("mongodb://127.0.0.1:27018/")
mydb = client["scrapy-database"]
db_collection = mydb['livres']

cursor = db_collection.find({})
p = ""

for document in cursor:
    p += '<div class="tale">\
                <div class="picture" style="background-image: url(\''+document["picture"]+'\')"></div>\
                <div class="title">'+document["title"]+'</div>\
                <div class="otherInformations">\
                    <div class="retail">'+document["availability"]+'</div>\
                    <div class="price">'+document["price"]+'$</div>\
                </div>\
                <div class="resume">'+document["description"]+'</div>\
            </div>'

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>Livres</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">%s</div>
</body>
</html>
'''%(p)

filename = 'index.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)

# if(client.is_connected()):
#     cursor.close()
#     client.close()
#     print("MongoDB connection is closed.")  