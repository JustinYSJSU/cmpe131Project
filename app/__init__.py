from flask import Flask

appObj = Flask(__name__)
appObj.config.from_mapping(SECRET_KEY = 'you-will-never-guess')

#from app import routes
