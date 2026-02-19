from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskr.models import Base

db = SQLAlchemy(model_class=Base)

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .accounting import routes
        from .directory import routes
        from .documents import routes
        from .nomenclature import routes
        from .reports import routes

        # Register Blueprints
        app.register_blueprint(accounting.accounting_bp)
        app.register_blueprint(directory.directory_bp)
        app.register_blueprint(documents.documents_bp)
        app.register_blueprint(nomenclature.nomenclature_bp)
        app.register_blueprint(reports.reports_bp)

        return app