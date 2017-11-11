# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
}
db=MongoEngine(app)
#db.init_app(app)


class User(db.Document):
    username=db.StringField()

@app.route('/', methods=['GET'])
def hello():
    return "hello world"


@app.route('/add', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = User(username=name)
    user.save()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


@app.route('/findd', methods=['GET'])
def find():
    name = request.args.get('name')
    user = User.objects(username=name)
    print(user)
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


if __name__ == "__main__":
    app.run(debug=True)