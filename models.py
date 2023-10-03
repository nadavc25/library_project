# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    book_type = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=1)

    def __init__(self, name, author, year_published, book_type, quantity=1):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "year_published": self.year_published,
            "book_type": self.book_type,
            "quantity": self.quantity
        }

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "age": self.age
        }

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    loan_date = db.Column(db.String(10))
    return_date = db.Column(db.String(10))

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
