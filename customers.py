# customers.py
from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Customer, db

customers_bp = Blueprint('customers', __name__)

@customers_bp.route("/", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    customer_list = [customer.to_dict() for customer in customers]
    return jsonify(customer_list)

@customers_bp.route("/", methods=["POST"])
def add_customer():
    data = request.json

    if not data:
        return jsonify({"message": "Invalid data"}), 400

    name = data.get("name")
    city = data.get("city")
    age = data.get("age")

    if not name or not city or not age:
        return jsonify({"message": "Missing data fields"}), 400

    # Create a new Customer object and add it to the database
    customer = Customer(name=name, city=city, age=age)
    db.session.add(customer)
    db.session.commit()

    return jsonify({"message": "Customer added successfully"}), 201

@customers_bp.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    return jsonify(customer.to_dict())

@customers_bp.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    data = request.json

    if not data:
        return jsonify({"message": "Invalid data"}), 400

    # Update the specified fields if they exist in the request data
    if "name" in data:
        customer.name = data["name"]
    if "city" in data:
        customer.city = data["city"]
    if "age" in data:
        customer.age = data["age"]

    db.session.commit()

    return jsonify({"message": "Customer updated successfully"})

@customers_bp.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    db.session.delete(customer)
    db.session.commit()

    return jsonify({"message": "Customer deleted successfully"})
