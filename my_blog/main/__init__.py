from flask import Blueprint

main = Blueprint('main', __name__)

from my_blog.main import routes