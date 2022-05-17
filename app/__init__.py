from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

#project base directory
basedir = os.path.abspath(os.path.dirname(__file__))

appObj = Flask(__name__)
appObj.config.from_mapping(
   SECRET_KEY = 'you-will-never-guess',
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
   )
appObj.config['TESTING'] = False

appObj.secret_key = "you-will-never-guess"

db = SQLAlchemy(appObj)
login = LoginManager(appObj)
login.login_view = 'login'

from app import routes, models
