import uuid
from flask import Flask, request
from db import items, stores
from flask_smorest import abort

app = Flask(__name__)

@app.get("/stores") #decorador para dizer que o método vai ser invocado ao receber um GET em /stores
def get_stores():
    return {"stores": list(stores.values())}

@app.get("/stores/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")
    
@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/items/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")

@app.post("/stores")
def create_store():
    store_data = request.get_json()

    if "name" not in store_data:
        abort(400, message="Ensure that the 'name' is included in the payload.")
    
    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message="Cannot add the same store more than once.")

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return stores[store_id], 201

# agora o id da loja é passado no payload
@app.post("/items")
def create_item():
    item_data = request.get_json()

    if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
        abort(400, message="Ensure that 'price', 'store_id' and 'name' are included in the payload.")

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    for item in items.values():
        if (item["name"] == item_data["name"] and item["store_id"] == item_data["store_id"]):
            abort(400, message="Cannot add the same item more than once.")

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return items[item_id], 201

@app.delete("/items/<string:item_id>")
def delete_item(item_id):
    try:
        return items.pop(item_id)
    except KeyError:
        abort(404, message="Item not found.")