from flask import render_template, redirect, url_for
from app import app, db


@app.route("/")
def index():
    return render_template("user_side_html/index.html")