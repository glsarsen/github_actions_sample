from flask import Flask
from config import Config
from app.main import bp


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize Flask extensions here

    # Register blueprints here
    app.register_blueprint(bp)

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"
    
    return app