from . import VERSION
from flask_restful import Resource
from app import api
from flask import jsonify,request
from datetime import datetime
from schedule.middleware import start_task,get_task_status

class Index(Resource):
    def get(self):
        return jsonify({'datetime':datetime.now()})

class Version(Resource):
    def get(self):
        return jsonify({'version':VERSION})

class Nbu(Resource):
    def post(self):
        request_body = request.json
        return start_task('nbu_start_or_stop',request_body['action'])

class Policys(Resource):
    def get(self):
        return start_task('get_policys')

class TaskStatus(Resource):
    def get(self,task_id):
        response = get_task_status(task_id)
        return jsonify(response)

api.add_resource(Index,'/')
api.add_resource(Version,'/version')
api.add_resource(Nbu,'/nbu/')
api.add_resource(Policys,'/nbu/policys/')
api.add_resource(TaskStatus,'/jobstatus/<task_id>')

