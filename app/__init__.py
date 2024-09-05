#!/usr/bin/python3

""" This script initializes and returns the app"""

from flask import Flask


def create_app():
    """This function creates and returns the app"""
    app = Flask(__name__)
    with app.app_context():
        from .routes import home_routes, service_routes
        from .routes import contact_routes, branch_routes
        app.register_blueprint(home_routes.bp)
        app.register_blueprint(service_routes.bp)
        app.register_blueprint(contact_routes.bp)
        app.register_blueprint(branch_routes.bp)
    return app
