import os
import json

class Config(object):
    DEBUG = False
    TESTING = False
    # MongoDB Info
    MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
    MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE")
    MONGODB_HOST = os.environ.get("MONGODB_HOST")
    MONGODB_PORT = os.environ.get("MONGODB_PORT")
    ALLOWED_HOST = os.environ.get("ALLOWED_HOST")

config = {"config": Config}