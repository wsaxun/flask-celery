from . import VERSION,api_bp as api
from flask import jsonify,request
from datetime import datetime
from schedule.middleware import start_task,get_task_status

@api.route('/')
def index():
    return jsonify({'datetime':datetime.now()})

@api.route('/version/')
def version():
    return jsonify({'version':VERSION})

@api.route('/nbu/',methods=['POST'])
def nbu_start_or_stop():
    request_body = request.json
    return start_task('nbu_start_or_stop',request_body['action'])

@api.route('/nbu/policys/')
def get_policys():
    return start_task('get_policys')

@api.route('/jobstatus/<task_id>')
def taskstatus(task_id):
    response = get_task_status(task_id)
    return jsonify(response)
