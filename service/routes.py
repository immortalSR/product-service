from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

@app.route("/products", methods=["GET"])
def list_products():
    return jsonify(products)

@app.route("/products/<int:pid>", methods=["GET"])
def read_product(pid):
    for p in products:
        if p["id"] == pid:
            return jsonify(p)
    return {}, 404

@app.route("/products", methods=["POST"])
def create_product():
    data = request.json
    products.append(data)
    return jsonify(data), 201

@app.route("/products/<int:pid>", methods=["PUT"])
def update_product(pid):
    for p in products:
        if p["id"] == pid:
            p.update(request.json)
            return jsonify(p)
    return {}, 404

@app.route("/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    global products
    products = [p for p in products if p["id"] != pid]
    return {}, 204
