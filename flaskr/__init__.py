from flask import Flask
from pydantic import ValidationError

from flaskr.database import db

from flaskr.models import *
from flaskr.directory.models import *
from flaskr.nomenclature.models import *
from flaskr.documents.models import *
from flaskr.bank.models import *


def init_app():
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # handle error from pydantic validation
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return {"errors": e.errors(include_context=False)}, 400

    db.init_app(app)

    with app.app_context():
        db.create_all()
        # Import parts of our application
        from .accounting import routes
        from .directory import urls
        from .documents import urls
        from .nomenclature import urls
        from .bank import urls
        from .reports import routes

        # Register Blueprints
        app.register_blueprint(accounting.routes.accounting_bp)
        app.register_blueprint(directory.directory_bp)
        app.register_blueprint(documents.documents_bp)
        app.register_blueprint(nomenclature.nomenclature_bp)
        app.register_blueprint(bank.bank_bp)
        app.register_blueprint(reports.routes.reports_bp)

        return app