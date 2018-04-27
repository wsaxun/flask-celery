import os
from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import User
from common.common import run_cmd

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

@app.shell_context_processor
def make_shell_context():
	return dict(
		db = db,
		User = User,
    )

@manager.command
def create_db():
	'''create all database'''
	db.create_all()

@manager.command
def test_db_insert():
	'''test insert data to databases'''
	user = User(name='greene',mail='example@163.com',password='123456')
	db.session.add(user)
	db.session.commit()

@manager.command
def start_celery():
	'''start celery'''
	cmd = 'celery -A schedule.app worker -l info'
	return run_cmd(cmd)

@manager.option('--action',help='nbu action.')
def nbu(action):
	'''nbu exec'''
	cmd = '/etc/init.d/netbackup %s'%action
	result = run_cmd(cmd)
	print(result)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('runserver',Server(
	use_debugger=True,use_reloader=True,
	host='0.0.0.0',port=8000
))

if __name__ == "__main__":
	manager.run()
