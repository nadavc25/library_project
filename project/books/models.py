# project/books/models.py
from project import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.Integer)
    book_type = db.Column(db.Integer)
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


    loans = db.relationship('Loan', back_populates='book')
