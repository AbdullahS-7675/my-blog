from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from my_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from my_blog.main.routes import main
    from my_blog.posts.routes import posts
    from my_blog.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)
    
    return app