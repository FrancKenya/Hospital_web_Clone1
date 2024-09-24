#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """This function creates and returns the app"""
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    

    with app.app_context():
        from .routes import home_routes, service_routes, contact_routes
        from .routes import branch_routes
        from .routes.booking_routes import booking_routes
        app.register_blueprint(home_routes.bp)
        app.register_blueprint(service_routes.bp)
        app.register_blueprint(contact_routes.bp)
        app.register_blueprint(branch_routes.bp)
        app.register_blueprint(booking_routes)

    return app
