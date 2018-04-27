from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
mail = Mail()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)

    # from .api_v_0_1 import api_bp
    # app.register_blueprint(api_bp,url_prefix='/api/v0.1')

    from .api_v_0_2 import api_0_2_bp
    api.init_app(api_0_2_bp)
    app.register_blueprint(api_0_2_bp,url_prefix='/api/v0.2')

    from .web import web_bp
    app.register_blueprint(web_bp)

    return app
