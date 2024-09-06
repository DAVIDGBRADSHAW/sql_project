#https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/legacy-query/
from statistics import median, mean
from flask import Flask, render_template, redirect, request, url_for
#import jsonpickle
from models import BlogPost, db

@app.route("/create", methods=["POST"])
def create_post_action():
    post = BlogPost(
        title=request.form["title"],
        content=request.form["content"],
        author=request.form["author"],
    )
    db.session.add(post)
    db.session.commit()
    return redirect(url_for("index"))

