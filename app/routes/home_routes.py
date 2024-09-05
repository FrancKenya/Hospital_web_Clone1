#!/usr/bin/python3

""" This script contains the routes for the home page. """

from flask import Blueprint, render_template

bp = Blueprint("home", __name__)


@bp.route("/")
def home():
    """renders the home page"""
    return render_template("home.html")
