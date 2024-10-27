from flask import Flask, jsonify, request
from logic.business_logic import Facade

app = Flask(__name__)
facade = Facade()

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

if __name__ == '__main__':
    app.run(debug=True)
