from flask import Flask, jsonify, request
from logic.business_logic import Facade
from logic.models.user import User
from storage.user_repository import UserRepository

app = Flask(__name__)
facade = Facade()
user_repo = UserRepository()

@app.route('/items/<item_id>', methods=['POST'])
def add_item(item_id):
    item = request.json
    facade.add_item(item_id, item)
    return jsonify({'message': 'Item added successfully'}), 201

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = facade.get_item(item_id)
    return jsonify(item) if item else jsonify({'message': 'Item not found'}), 404

@app.route('/items/<item_id>', methods=['DELETE'])
def remove_item(item_id):
    facade.remove_item(item_id)
    return jsonify({'message': 'Item removed successfully'}), 200

@app.route('/api/v1/users/', methods=['POST'])
def add_user():
    data = request.json
    user = User(email=data['email'], password=data['password'])
    user_repo.add(user)
    return jsonify(user.__dict__), 201

@app.route('/api/v1/users/', methods=['GET'])
def get_users():
    users = user_repo.get_all()
    return jsonify([user.__dict__ for user in users]), 200

@app.route('/api/v1/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_repo.get(user_id)
    if user:
        return jsonify(user.__dict__), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/v1/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = user_repo.get(user_id)
    if user:
        data = request.json
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        user_repo.update(user)
        return jsonify(user.__dict__), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
