from flask import Blueprint

# Blueprint Configuration
nomenclature_bp = Blueprint(
    'nomenclature_bp', __name__, url_prefix='/nomenclature',
)