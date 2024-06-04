from flask import Blueprint

users = Blueprint('users', __name__)

from my_blog.users import routes