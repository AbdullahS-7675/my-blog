from flask import Blueprint, render_template
from datetime import datetime
from my_blog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', title='Home', posts = posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')