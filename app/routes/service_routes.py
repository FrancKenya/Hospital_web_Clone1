#!usr/bin/python3
""" This module contains the routes for the services page """
from flask import Blueprint, render_template

bp = Blueprint("services", __name__)


@bp.route("/services")
def services():
    """renders the services page"""
    return render_template("services.html")
