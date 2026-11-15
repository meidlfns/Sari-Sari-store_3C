from flask import Flask, jsonify, request
from data import products

sss = Flask(__name__)

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