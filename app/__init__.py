from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import config
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .web import web_bp
    app.register_blueprint(web_bp)

    return app
