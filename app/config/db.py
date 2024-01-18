from pymongo import MongoClient

from .settings import settings

MongoClient = MongoClient(settings.mongo_url)
db = MongoClient.UserData
