from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register blueprints or routes
    from .user_routes import user_bp  # Example: Import a Blueprint
    app.register_blueprint(user_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
