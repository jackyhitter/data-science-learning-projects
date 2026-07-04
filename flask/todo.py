from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

items = [
    {"id":1, "title" : "item1", "task" : "regarding item1"},
    {"id":2, "title" : "item2", "task" : "regarding item2"},
    {"id":3, "title" : "item3", "task" : "regarding item3"}
]

@app.route('/')
def home():
    return "Welcome to the Sample Todo App"

@app.route('/items', methods=['GET'])
def getItems():
    return jsonify(items)

## get by id

@app.route('/items/<int:id>', methods=['GET'])
def getItem(id):
    item = next((item for item in items if item['id'] == id), None)
    if item == None:
        return jsonify({"error": "item not found"}), 404
    return jsonify(item)

## create a new item using post method
@app.route('/items', methods=['POST'])
def createItem():
    if not request.json or not 'title' in request.json or not 'task' in request.json:
        return jsonify({"error": "BAD REQUEST"}), 400
    newItem = {
        "id" : items[-1]["id"]+1,
        "title" : request.json['title'],
        "task" : request.json['task']
    }
    items.append(newItem)
    return jsonify(newItem), 201

## Updating an Item using PUT method
@app.route('/items/<int:id>', methods=['PUT'])
def updateItem(id):
    if not request.json:
        return jsonify({"error": "BAD REQUEST"}), 400
    item = next((item for item in items if item["id"] == id), None)
    if item == None:
        return jsonify({"error": "item not found"}), 404
    item['title'] = request.json.get('title', item['title'])
    item['task'] = request.json.get('task', item['task'])
    return jsonify(item), 200

## delete operation
@app.route('/items/<int:id>', methods=['DELETE'])
def deleteItem(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({"result": "item deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)