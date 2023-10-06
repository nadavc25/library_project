# project/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)

    db_path = os.path.join(instance_path, 'library.db')
    print(f"Database path: {db_path}")  # for debug

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off tracking modifications

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from project.books.books import books_bp
    from project.customers.customers import customers_bp
    from project.loans.loans import loans_bp

    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(loans_bp, url_prefix='/loans')

    with app.app_context():
        db.create_all()  # Create tables within the application context

    return app
