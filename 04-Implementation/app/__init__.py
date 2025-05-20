"""App initialization."""
from flask import Flask
from .routes import chat

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat)
    @app.errorhandler(500)
    def internal_error(error):
     return f"500 error: {error}", 500

    return app