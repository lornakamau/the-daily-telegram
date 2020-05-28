from flask import Flask
from .config import DevConfig

app = Flask(__name__) #instance of app

app.config.from_object(DevConfig) #setting up configuration

from app import views