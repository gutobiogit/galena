"""Routing and processing data RESTview

Returns:
    _type_: json
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import controller


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/v1/data/<int:row_id>', methods=['GET'])
def get_one(row_id):
    output = controller.get_one_data(row_id)
    return jsonify(output)


@app.route('/v1/data', methods=['GET'])
def get_all():
    output = controller.get_all_data()
    return jsonify(output)


@app.route('/v1/data', methods=['POST'])
def add_data():
    message = controller.create_new_record(request.json)
    return jsonify({'message': message})


@app.route('/v1/data/<int:row_id>', methods=['PUT'])
def change_data(row_id):
    message = controller.change_record(row_id, request.json)
    return jsonify({'message': message})


@app.route('/v1/data/<int:row_id>', methods=['DELETE'])
def delete_data(row_id):
    message = controller.delete_record(row_id)
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
