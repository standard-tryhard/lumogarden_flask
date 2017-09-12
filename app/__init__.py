from flask import Flask
from flask_pymongo import PyMongo
from whitenoise import WhiteNoise

lumo_hub = Flask(__name__)
lumo_hub.config.from_object('config')

client = MongoClient(lumo_hub.MONGO_URI)
db = client[lumo_hub.MONGO_DBNAME]

lumo_hub.wsgi_app = WhiteNoise(lumo_hub.wsgi_app, root='static/')

from app import views
