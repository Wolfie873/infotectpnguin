import pymongo
import pprint

from pymongo import MongoClient
client = MongoClient()

db = client.bookstore
books = db.books
pprint.pprint(books.find_one({"title": "Blue"}))