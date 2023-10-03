from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db
from books import books_bp
from customers import customers_bp
from loans import loans_bp
import os

instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)
db_path = os.path.join(instance_path, 'library.db')
print(f"Database path: {db_path}")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off tracking modifications

# Create 'instance' directory if it doesn't exist

db.init_app(app)


CORS(app)

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(loans_bp, url_prefix='/loans')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True, port=5000)
