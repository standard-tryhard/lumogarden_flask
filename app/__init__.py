from flask import Flask
from flask_pymongo import PyMongo
# from flask_script import Manager
from whitenoise import WhiteNoise

lumo_hub = Flask('lumogrids')
lumo_hub.config.from_object('config')
# mongo = PyMongo(lumo_hub)
lumo_hub.wsgi_app = WhiteNoise(lumo_hub.wsgi_app, root='static/')

from app import views
