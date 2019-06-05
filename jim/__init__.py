from flask import Flask, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate
from . import Config
import os

application = Flask(__name__)

if os.getenv('APP_ENV') == 'DEV':
    application.config.from_object(Config.DevelopmentConfig)
elif os.getenv('APP_ENV') == 'PROD':
    application.config.from_object(Config.ProductionConfig)

db = SQLAlchemy(application)
migrate = Migrate(application, db)

from jim import views
from jim.models import *
