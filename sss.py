from itertools import product

from flask import Flask, jsonify, request

sss = Flask(__name__)

{
    "products": [
        {"product_id": 1, "name": "Sunsilk", "price": 8, "stock": 75}
        {"product_id": 2, "name": "555 Sardines", "price": 35, "stock": 105},
        {"product_id": 3, "name": "DingDong":, "price": 15, "stock": 24}
    ]
}

@sss.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products}), 200

if __name__ == '__main__':
    sss.run(debug=True)