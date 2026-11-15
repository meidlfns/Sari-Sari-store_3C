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
    return jsonify(products), 200

@sss.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products["products"] if p["product_id"] == id), None)
    if product is None:
        return jsonify({"error": "Products Not Found"}), 404
    return jsonify(product), 200

if __name__ == '__main__':
    sss.run(debug=True)