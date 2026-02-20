from flask import Blueprint

directory_bp = Blueprint(
    'directory_bp', __name__, url_prefix='/directory'
)


from .organization import *