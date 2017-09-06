from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from whitenoise import WhiteNoise

app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import views, models
