from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#project base directory
basedir = os.path.abspath(os.path.dirname(__file__))

appObj = Flask(__name__)
appObj.config.from_mapping(
   SECRET_KEY = 'you-will-never-guess',
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
   )

db = SQLAlchemy(appObj)

from app import models #, routes
