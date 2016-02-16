#!/usr/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

#Set up API for Add function
@app.route('/api/v1.0/add', methods=['POST'])
def add():
    if not request.json or not 'x' in request.json or not 'y' in request.json:
        abort(400)
    x = request.json.get('x')
    y = request.json.get('y')
    return jsonify({'val': x+y})


if __name__ == '__main__':
    app.run(debug=True)
