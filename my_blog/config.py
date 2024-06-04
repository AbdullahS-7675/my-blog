import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'frn3&*&fge'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
