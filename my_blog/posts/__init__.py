from flask import Blueprint

posts = Blueprint('posts', __name__)

from my_blog.posts import routes
