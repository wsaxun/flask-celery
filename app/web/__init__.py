from flask import Blueprint

web_bp = Blueprint('webbp',__name__)

from . import view
