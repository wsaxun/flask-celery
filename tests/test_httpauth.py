from flask import Flask,g,request,jsonify
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfdfdkjfdkj'
serializer = Serializer(app.config['SECRET_KEY'],expires_in=1800)
auth = HTTPTokenAuth(scheme='Token')

tokens = {
    "Greene":"123456",
}

@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = serializer.loads(token)
    except:
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False

@app.route('/')
@auth.login_required
def index():
    return "Hello,%s!"%g.current_user

@app.route('/token/',methods=['POST'])
def get_token():
    if request.method == 'POST':
        print(request.json)
        # jsondata = json.loads(request.data)
        # token = serializer.dumps({'username': jsondata['user'],'password':jsondata['password']})
        # return jsonify({'token':token})
        return ''
    return ''



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8000)
