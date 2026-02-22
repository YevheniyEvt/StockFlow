from flask import Blueprint

accounting_bp = Blueprint(
    'accounting_bp', __name__, url_prefix='/accounting'
)