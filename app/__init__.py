from flask import Flask
from flask_pymongo import PyMongo
from whitenoise import WhiteNoise

lumo_hub = Flask(__name__)
lumo_hub.config.from_object('config')
lumo_hub.wsgi_app = WhiteNoise(lumo_hub.wsgi_app, root='static/')
mongo = PyMongo(lumo_hub)

from app import views
