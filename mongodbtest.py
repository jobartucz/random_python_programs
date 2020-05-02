import pymongo

# you will need to change this connection string to match your own instance
client = pymongo.MongoClient("mongodb+srv://Ben:breger2020@cluster0-uyp2d.gcp.mongodb.net/test?retryWrites=true&w=majority")
# remember that if you have special characters in your password, you need to "escape" them
# or import and use urllib.parse.quote_plus
# More info: https://pymongo.readthedocs.io/en/stable/examples/authentication.html
# Ascii codes: https://ascii.cl/

mydb = client.test

mydb = client["sample_airbnb"]
mycollection = mydb["listingsAndReviews"]

mydocument = mycollection.find_one({"name":"White House"})
print(mydocument)