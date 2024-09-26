#!/usr/bin/python3
""" This module contains the routes for the migrations page """

from flask import Blueprint, render_template
from flask_migrate import upgrade
from flask import current_app


migration_bp = Blueprint("migration_bp", __name__)


@migration_bp.route('/trigger-migration', methods=['GET'])
def run_migration():
    """Route to run db migrations"""
    try:
        upgrade()
        return "Migration successful!", 200
    except Exception as e:
        return f"Migration failed: {e}", 500
