import os
from pymongo import MongoClient
from app import lumo_hub

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess' #make it really hard when it's deployed

lumo_hub.config['MONGO_DBNAME'] = 'lumogrids_flask'
lumo_hub.config['MONGO_URI'] = 'mongodb://localhost:27017/lumogrids_flask'

