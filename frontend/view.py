from PIL import Image
from flask import Flask, render_template, url_for, flash, redirect, request
#from frontend import app, db, bcrypt
from datetime import datetime
import requests

app = Flask(__name__)
@app.route("/", methods = ['GET'])
def home():
    return render_template("home.html",
                           posts=requests.get("https://hackthevalley.herokuapp.com/").json())

@app.route("/post/new", methods = ['GET', 'POST'])
def new_post():
    # post=Post(title=form.title.data, content = form.content.data, date = datetime.now())
    if request.method == "POST":
        pass
    return render_template("insert.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

 #@app.route('/post/<post_id>')
## def post(post_id):
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template("post.html", title=post.title, post=post)

#routes,form for post

#git add *
#git commit -m "sdfsadfasdf"
#git push

#git pull
