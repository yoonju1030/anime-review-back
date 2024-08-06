import os
import json

class Config(object):
    DEBUG = False
    TESTING = False
    # MongoDB Info
    MONGODB_USERNAME = os.environ["MONGODB_USERNAME"]
    MONGODB_PASSWORD = os.environ["MONGODB_PASSWORD"]
    MONGODB_DATABASE = os.environ["MONGODB_DATABASE"]
    MONGODB_HOST = os.environ["MONGODB_HOST"]
    MONGODB_PORT = os.environ["MONGODB_PORT"]
    ALLOWED_HOST = os.environ["ALLOWED_HOST"]

config = {"config": Config}