# app.py
from flask import render_template
from project import create_app, db

app = create_app()

@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)