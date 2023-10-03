# database.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from models import Book, Customer, Loan

# Create a SQLite database file
engine = create_engine('sqlite:///instance/library.db?foreign_keys=on', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the Books model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    year_published = Column(Integer)
    book_type = Column(Integer)
    quantity = Column(Integer, default=1)

    loans = relationship('Loan', back_populates='book')

# Define the Customers model
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    age = Column(Integer)

    loans = relationship('Loan', back_populates='customer')

# Define the Loans model
class Loan(Base):
    __tablename__ = 'loans'
    
    id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    loan_date = Column(Date)
    return_date = Column(Date, nullable=True)  # Nullable, as initially, it's not returned

    customer = relationship('Customer', back_populates='loans')
    book = relationship('Book', back_populates='loans')
