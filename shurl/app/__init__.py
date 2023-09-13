from pymongo import MongoClient


client = MongoClient("mongodb://host.docker.internal:27017/")
db_client = client["shurl_db"]
