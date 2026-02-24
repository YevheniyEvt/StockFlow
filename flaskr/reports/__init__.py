from flask import Blueprint

# Blueprint Configuration
reports_bp = Blueprint(
    'reports_bp', __name__, url_prefix='/reports',
)