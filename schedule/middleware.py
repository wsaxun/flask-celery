from .task_msg import task_started_msg,task_started_error_msg
import time
from .app import app
from .tasks import test_task

def start_task(task_name,params=None):
    try:
        task = None
        if task_name == 'test_task':
            task = test_task.delay(params)
        return task_started_msg(task.id)
    except Exception as ex:
        return task_started_error_msg(ex)

def get_task_status(task_id):
    task = app.AsyncResult(task_id)
    if task.state == 'STARTED':
        response = {
            'jobid':task_id,
            'description':'',
            'status':'running',
            'state':'',
            'comment':'task is running'
        }
    elif task.state == 'PENDING':
        response = {
            'jobid':task_id,
            'description':'',
            'status':'running',
            'state':'',
            'comment':'task is pending'
        }
    elif task.state == 'FAILURE':
        response = task.result
        response['jobid'] = task_id
        response['status'] = 'completed'
    else:
        response = {
            'jobid':task_id,
            'description':str(task.info),
            'status':'completed',
            'state':'success',
        }
    return response

