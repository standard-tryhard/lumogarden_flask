from flask import Flask
from whitenoise import WhiteNoise


lumo_hub = Flask(__name__)
lumo_hub.config['SECRET_KEY'] = 'SECRET!'
lumo_hub.config.from_object('config')
# lumo_hub.wsgi_app = WhiteNoise(lumo_hub.wsgi_app, root='app/static')


from app import views
