from flask import Flask,request,jsonify,json

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/test/',methods=['POST'])
def test():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + str(request.data)

    elif request.headers['Content-Type'] == 'application/json':
        # return "JSON Message: " + json.dumps(request.json)
        json = request.json

        return jsonify({
            'data':json,

        })

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

