# app/__init__.py
# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# local imports
from instance.config import app_config
# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    from app import models

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .freelancers import freelancers as freelancers_blueprint
    app.register_blueprint(freelancers_blueprint)

    from .market import market as market_blueprint
    app.register_blueprint(market_blueprint)

    from .agency import agency as agency_blueprint
    app.register_blueprint(agency_blueprint)


    return app