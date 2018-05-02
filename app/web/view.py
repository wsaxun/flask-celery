from . import web_bp
from flask import request
from schedule.middleware import start_task

@web_bp.route('/')
def index():
    return '<h2>test page</h2>'

@web_bp.route('/test/')
def test():
    return start_task('test_task',params='param1')

