from flask import Flask

# Initialize Firestore DB

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '@#$%^&*(SDFGHJ#$%^&!*('

    from .api import api

    app.register_blueprint(api, url_prefix='/api')

    return app
