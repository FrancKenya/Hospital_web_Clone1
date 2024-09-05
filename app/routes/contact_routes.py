#!/usr/bin/python3

""" This module contains the routes for the contacts page """

from flask import Blueprint, render_template

bp = Blueprint("contact", __name__)


@bp.route("/contact")
def contact():
    """renders the contact page"""
    return render_template("contact.html")
