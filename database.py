# database.py
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# Create a SQLite database file
engine = create_engine('sqlite:///instance/library.db?foreign_keys=on', echo=True)

# Create a base class for declarative models
Base = declarative_base()

db = SQLAlchemy()
migrate = Migrate()
