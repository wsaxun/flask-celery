from flask import jsonify
from datetime import datetime

def task_started_msg(task_id):
    return jsonify({
        'status': 'start successful',
        'jobid':task_id,
        'time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

def task_started_error_msg(des):
    return jsonify({
        'state':'start failed',
        'error':str(des)
    })
