#!/usr/bin/python3

""" This module contains the migration routes flask
configuration """

from flask import Blueprint, render_template
from flask_migrate import upgrade

migrate_routes = Blueprint('migrate_routes', __name__)

@migrate_routes.route('/migrate-db')
def migrate_db():
    """upgrade database"""
    try:
        upgrade()
        return "Database migration successful!", 200
    except Exception as e:
        return f"Migration failed: {str(e)}", 500
