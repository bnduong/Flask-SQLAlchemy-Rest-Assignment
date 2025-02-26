from flask import Flask, request, jsonify
from flask-sqlalchemy import SQLAlchemy
from flask-marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLALCHEMY(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
 id = db.Column(db.Interger, primary_key=True)
 name = db.Column(db.String(100), unique=True)
 description = db.Column(db.String(200))
 price = db.Column(db.Float)
 qty = db.Column(db.Interger)

 def __init__(self, name, description, price, qty):
   self.name = name
   self.description = description
   self.price = price
   self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
   class Meta:
       fields = ('id', 'name', 'description', 'price', 'qty')

# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

new_product = Product(name, description, price, qty)

db.session.add(new_product)
db.session.commit()

return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Get Single Product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id)
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)
# Run Server
if __name__ == '__main__':
 app.run(debug=True)
