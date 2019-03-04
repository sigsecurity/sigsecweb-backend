from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from sqlalchemy_utils import database_exists
from sqlalchemy.engine.url import make_url
import os


def create_app(config='sigsec.config.Config'):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(config)

    with app.app_context():
        from sigsec.database import db

        from sigsec.auth import auth
        app.register_blueprint(auth)

    return app
