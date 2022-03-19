from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "database.db"

# FLASK
def create_app():

    app = Flask(__name__)
    app.secret_key = "hello"
    app.config['SQLALCHEMY_DATABSE_URI'] = f'sqlite:///{DB_NAME}.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .screen import screen
    app.register_blueprint(screen, url_prefix='/')

    from .models import musiclist

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')
