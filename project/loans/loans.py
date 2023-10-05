# loans.py
from datetime import datetime
from flask import Blueprint, request, jsonify

from project import db
from project.loans.models import Loan


def __init__(self, cust_id, book_id, loan_date, return_date=None):
        self.cust_id = cust_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

def to_dict(self):
        return {
            "id": self.id,
            "cust_id": self.cust_id,
            "book_id": self.book_id,
            "loan_date": self.loan_date,
            "return_date": self.return_date
        }

loans_bp = Blueprint('loans', __name__)



def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False


@loans_bp.route("/", methods=["GET"])
def get_loans():
    loans = Loan.query.all()
    loan_list = [loan.to_dict() for loan in loans]
    return jsonify(loan_list)

@loans_bp.route("/", methods=["POST"])
def add_loan():
    try:
        db.session.begin()
        data = request.json
        cust_id = data.get("cust_id")
        book_id = data.get("book_id")
        
        # Set the loan_date to the current date and time
        loan_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return_date = data.get("return_date")

        if not cust_id or not book_id or not loan_date:
            return jsonify({"message": "Missing data fields"}), 400

        if not validate_date(loan_date) or (return_date and not validate_date(return_date)):
            return jsonify({"message": "Invalid date format"}), 400

        if return_date and loan_date > return_date:
            return jsonify({"message": "Loan date cannot be after return date"}), 400

        # Create a new Loan object and add it to the database
        loan = Loan(cust_id=cust_id, book_id=book_id, loan_date=loan_date, return_date=return_date)
        db.session.add(loan)
        db.session.commit()

        return jsonify({"message": "Loan added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500
    finally:
        db.session.close()

@loans_bp.route("/<int:loan_id>", methods=["GET"])
def get_loan(loan_id):
    loan = Loan.query.get(loan_id)
    
    if not loan:
        return jsonify({"message": "Loan not found"}), 404
    
    return jsonify(loan.to_dict())

@loans_bp.route("/<int:loan_id>", methods=["PUT"])
def return_loan(loan_id):
    loan = Loan.query.get(loan_id)
    
    if not loan:
        return jsonify({"message": "Loan not found"}), 404
    
    data = request.json

    if not data:
        return jsonify({"message": "Invalid data"}), 400

    # Update the return date to the current date and time when returning the loan
    loan.return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    db.session.commit()
    
    return jsonify({"message": "Loan returned successfully"})
