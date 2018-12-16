from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate 
from flask_login import LoginManager

from flask_bootstrap import Bootstrap

from flask_pymongo import PyMongo

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()
mongo = PyMongo()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    Bootstrap(app)
    db.init_app(app)

    app.config['MONGO_DBNAME'] = 'easbdt'
    app.config['MONGO_URI'] = 'mongodb://didin:didin@cluster0-shard-00-00-cgiec.mongodb.net:27017,cluster0-shard-00-01-cgiec.mongodb.net:27017,cluster0-shard-00-02-cgiec.mongodb.net:27017/easbdt?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
    
    mongo.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)


    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)


    return app

