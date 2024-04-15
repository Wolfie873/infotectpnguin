import pymongo
import pprint

from pymongo import MongoClient
client = MongoClient()

db = client.bookstore
books = db.books

for book in books.find():
    pprint.pprint(book)