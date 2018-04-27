from . import web_bp
from flask import request

@web_bp.route('/')
def index():
    return '<h2>test page</h2>'
