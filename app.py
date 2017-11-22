# encoding: utf-8
from models import User
from flask import Flask, request, jsonify
from extensions import db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
}

db.init_app(app)


@app.route('/', methods=['GET'])
def hello():
    return "hello world"


@app.route('/create', methods=['POST'])
def create_user():
    name = request.form['name']
    psword=request.form['password']
    print(name,psword)
    user = User(username=name,password=psword)
    user.save()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


@app.route('/find', methods=['GET'])
def find():
    name = request.args.get('name')
    user = User.objects(username=name)
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


@app.route('/login', methods=['POST'])
def login():
    name=request.form['name']
    psword=request.form['password']
    user=User.objects(username=name,password=psword)
    if not user:
        return jsonify({'error':'password wrong'})
    else:
        return jsonify({'success':'login'})

if __name__ == "__main__":
    app.run(debug=True)