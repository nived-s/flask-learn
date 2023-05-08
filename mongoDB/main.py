from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# reading password from .env

# automatically loading env file
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

# Connecting to mongodb atlas
connection_string = f"mongodb+srv://nvd:{password}@cluster0.drm3sap.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()
print(dbs)

# accessing db
test_db = client.test_database

# accessing collections
collections = test_db.list_collection_names()
print(collections)



