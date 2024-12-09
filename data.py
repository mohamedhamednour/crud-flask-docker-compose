from flask import Flask, jsonify
import datetime
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    data = {"name": "hamed,o", "age": 30, "is_active": True}
    return jsonify(data)


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(data), 201


@app.route('/read/<int:user_id>', methods=['GET'])
def read(user_id):
    data = {'name': 'hamed,o', 'age': 30, 'is_active': True}
    return jsonify(data)


@app.route('/update/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    return jsonify(data)


@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Enable debug mode for auto-reload
