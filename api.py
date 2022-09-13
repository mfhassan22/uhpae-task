#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder="views")

users_model = []
users_model.append({"id": 1, "user": "bob", "number": "7236198"})
users_model.append({"id": 2, "user": "harry", "number": "21378123"})


@app.route('/api/')
def index():
    return jsonify({'action': 'testing',
                    'message': 'testing setup'})


@app.route('/api/users/', methods=['GET'])
def get_users():
    return jsonify(users_model)


@app.route('/api/users/', methods=['POST'])
def save_users():
    data = request.get_json()
    if (len(users_model) > 0):
        next_id = max(user['id'] for user in users_model)+1
        users_model.append(
            {'id': next_id, 'user': data['user'], 'number': data['number']})
        return jsonify({'result': 'Success', 'message': 'new user added'})
    else:
        users_model.append(
            {'id': 1, 'user': data['user'], 'number': data['number']})
        return jsonify({'result': 'Success', 'message': 'new user added'})


@app.route('/api/users/<int:id>', methods=['POST'])
def update_users(id):
    data = request.get_json()
    flage = False
    for user in users_model:
        if user['id'] == id:
            flage = True
            user.update({'user': data['user'], 'number': data['number']})
            return jsonify({'result': 'Success', 'message': 'user data updated'})

    if (flage == False):
        return jsonify({'result': 'Failure', 'message': 'user not found'})


@app.route('/')
def home():
    return render_template('index.html', users=users_model)


app.run()
