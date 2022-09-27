from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db_client = client["shurl_db"]
