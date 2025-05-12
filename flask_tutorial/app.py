from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Store 1",
        "active": True,
        "items": [
            {
                "name": "Chair",
                "price": 100.00
            },
            {
                "name": "Desk",
                "price": 200.00
            },
        ]
    },
    {
        "name": "Store 2",
        "active": True,
        "items": [
            {
                "name": "Bed",
                "price": 300.00
            },
            {
                "name": "Wardrobe",
                "price": 500.00
            },
        ]
    }
]

@app.get("/stores") #decorador para dizer que o método vai ser invocado ao receber um GET em /stores
def get_stores():
    return {"stores": stores}

@app.post("/stores")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "active": True, "items": request_data["items"]}
    stores.append(new_store)
    return new_store, 201

@app.post("/stores/<string:name>/item")
def create_item(name):
    item = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": item["name"], "price": item["price"]}
            store["items"].append(new_item)
            return item,201
    return {"message": "Store not found"}, 404

@app.get("/stores/<string:name>/items")
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return store["items"], 200
    return {"message": "Store not found"}, 404
