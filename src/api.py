"""Routing and processing data RESTapi

Returns:
    _type_: json
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import dto


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/v1/data/<int:row_id>', methods=['GET'])
def get_one(row_id):
    output = dto.get_one_data(row_id)
    return jsonify(output)


@app.route('/v1/data', methods=['GET'])
def get_all():
    output = dto.get_all_data()
    return jsonify(output)


@app.route('/v1/data', methods=['POST'])
def add_data():
    message = dto.create_new_record(request.json)
    return jsonify({'message': message})


@app.route('/v1/data/<int:row_id>', methods=['PUT'])
def change_data(row_id):
    message = dto.change_record(row_id, request.json)
    return jsonify({'message': message})


@app.route('/v1/data/<int:row_id>', methods=['DELETE'])
def delete_data(row_id):
    message = dto.delete_record(row_id)
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
