from pymongo import MongoClient
import conf

client=MongoClient(conf.mongo_uri,connect=False)