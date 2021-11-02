# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app import config
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask("balance")

#Cors policy
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(config)
db = SQLAlchemy(app)




#app.config['SECRET_KEY'] = 'random'
# app.debug = True
# toolbar = DebugToolbarExtension(app)
from app import config


from app.controllers import *