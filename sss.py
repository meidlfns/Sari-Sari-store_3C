from flask import Flask, jsonify, request

sss = Flask(__name__)

products = {
    "products": [
        {"product_id": 1, "name": "Sunsilk", "price": 8, "stock": 75},
        {"product_id": 2, "name": "555 Sardines", "price": 35, "stock": 105},
        {"product_id": 3, "name": "DingDong", "price": 15, "stock": 24}
    ]
}

@sss.route('/products', methods=['GET'])
def get_products():
    if not products:
        return jsonify({
            "error": "Internal Server Error",
            "message": "Unable to retrieve product information. Please try again later."
        }), 500
    return jsonify(products), 200

@sss.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products["products"] if p["product_id"] == id), None)
    if product is None:
        return jsonify({"error": "Products Not Found"}), 404
    return jsonify(product), 200

@sss.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "stock" not in data:
        return jsonify({
            "error": "Bad Request",
            "message": "Please provide all required product information, including name, price, and stock."
        }), 400
    
    new_id = max([p["product_id"] for p in products["products"]], default=0) + 1
    new_product = {
        "message": "Product added successfully.",
        "product_id": new_id,
            "name": data["name"],
            "price": data["price"],
            "stock": data["stock"]
    } 

    products["products"].append(new_product)
    return jsonify(new_product), 201
@sss.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = next((p for p in products["products"] if p["product_id"] == id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    if data:
        if "name" in data:
            product["name"] = data["name"]
        if "price" in data:
            product["price"] = data["price"]
        if "stock" in data:
            product["stock"] = data["stock"]

    return jsonify({
        "message": "Product updated successfully.",
        "product": product
    }), 200

@sss.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    product = next((p for p in products["products"] if p["product_id"] == id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    products["products"] = [p for p in products["products"] if p["product_id"] != id]
    return jsonify({
        "message": "Product deleted successfully.",
        "product": product
    }), 200

if __name__ == '__main__':
    sss.run(debug=True)