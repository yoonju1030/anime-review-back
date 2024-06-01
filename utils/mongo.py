from pymongo.mongo_client import MongoClient
from utils.config import Config
import urllib.parse

class MongoDB():
    def __init__(self):
        self.db = self.load_mongodb()

    def load_mongodb(self):
        mongodb_info = {
            "username": Config.MONGODB_USERNAME,
            "password": Config.MONGODB_PASSWORD,
            "host": Config.MONGODB_HOST,
            "port": Config.MONGODB_PORT,
        }
        mongo_db_client = self.create_mongodb_client(
            mongodb_info["username"],
            mongodb_info["password"],
            mongodb_info["host"],
            mongodb_info["port"],
        )
        db = self.get_mongodb_database(mongo_db_client, Config.MONGODB_DATABASE)
        return db
    def get_mongodb_database(self, client, database_name):
        mongo_db = client.get_database(database_name)
        return mongo_db
    
    def create_mongodb_client(self, user_name, password, host, port):
        mongo_db_client = MongoClient(
            f"mongodb://{user_name}:{urllib.parse.quote_plus(password)}@{host}:{port}"
        )
        return mongo_db_client
    
    def get_one_data(self, mongo_db, collection_name, query=None, sort=None, sort_type=1):
    
        if query is None and sort is None:
            selected_data = mongo_db[collection_name].find_one()
        elif query is None and sort is not None:
            selected_data = mongo_db[collection_name].find_one().sort(sort, sort_type)
        elif query is not None and sort is None:
            selected_data = mongo_db[collection_name].find_one(query)
        elif query is not None and sort is not None:
            selected_data = mongo_db[collection_name].find_one(query).sort(sort, sort_type)

        return selected_data
    
    def get_many_data(self, mongo_db, collection_name, query=None, sort=None, sort_type=1):
        if query is None and sort is None:
            selected_data = mongo_db[collection_name].find()
        elif query is None and sort is not None:
            selected_data = mongo_db[collection_name].find().sort(sort, sort_type)
        elif query is not None and sort is None:
            selected_data = mongo_db[collection_name].find(query)
        elif query is not None and sort is not None:
            selected_data = mongo_db[collection_name].find(query).sort(sort, sort_type)

        return selected_data