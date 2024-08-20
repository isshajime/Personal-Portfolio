from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENVIRONMENT = environ.get("ENVIRONMENT")
    # FLASK_APP = environ.get("FLASK_APP")
    FLASK_APP = 'wsgi.py'
    # SECRET_KEY = environ.get("FLASK_KEY")
    SECRET_KEY = 'demo_key'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI") 