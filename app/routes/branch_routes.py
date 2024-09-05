#!/usr/bin/python3

""" This module contains the branch routes flask
configuration """

from flask import Blueprint, render_template

bp = Blueprint("branches", __name__)


@bp.route("/branches")
def branches():
    """renders the branches page"""
    return render_template("branches.html")
