# project/loans/models.py
from project import db  # Import the db object from the database module

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    loan_date = db.Column(db.Date)
    return_date = db.Column(db.Date, nullable=True)

    customer = db.relationship('Customer', back_populates='loans')
    book = db.relationship('Book', back_populates='loans')

    def to_dict(self):
        # Get the related customer and book objects
        customer = self.customer
        book = self.book

        # Define the dictionary representation of the Loan object
        return {
            'id': self.id,
            'customer_name': customer.name if customer else '',  # Use the customer's name if it exists
            'book_title': book.title if book else '',  # Use the book's title if it exists
            'loan_date': self.loan_date.strftime('%Y-%m-%d %H:%M:%S'),  # Format as needed
            'return_date': self.return_date.strftime('%Y-%m-%d %H:%M:%S') if self.return_date else None,  # Format as needed
        }