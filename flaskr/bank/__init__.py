from flask import Blueprint

bank_bp = Blueprint(
    'bank_bp', __name__, url_prefix='/bank'
)