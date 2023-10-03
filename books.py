# books.py
from flask import Blueprint, jsonify, request
from models import Book, db

books_bp = Blueprint('books_bp', __name__)

@books_bp.route("/", methods=["GET"])
def get_books():
    print("Reached get_books() function")  # line for debugging
    books = Book.query.all()
    book_list = [book.to_dict() for book in books]
    return jsonify(book_list)

@books_bp.route("/", methods=["POST"])
def add_book():
    try:
        data = request.json

        print("Received data:", data)  #  line for debugging

        if not data:
            return jsonify({"message": "Invalid data"}), 400

        name = data.get("name")
        author = data.get("author")
        year_published = int(data.get("year_published"))
        book_type = int(data.get("book_type"))

        if not name or not author or not year_published or not book_type:
            return jsonify({"message": "Missing data fields"}), 400

        if book_type not in [1, 2, 3]:
            return jsonify({"message": "Invalid book_type"}), 400

        # Create a new Book object and add it to the database
        book = Book(name=name, author=author, year_published=year_published, book_type=book_type)
        db.session.add(book)
        db.session.commit()

        return jsonify({"message": "Book added successfully"}), 201
    except Exception as e:
        print("Error:", str(e))  # Add this line for debugging
        db.session.rollback()
        return jsonify({"message": str(e)}), 500
    finally:
        db.session.close()

@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    data = request.json

    if not data:
        return jsonify({"message": "Invalid data"}), 400

    # Update the specified fields if they exist in the request data
    if "name" in data:
        book.name = data["name"]
    if "author" in data:
        book.author = data["author"]
    if "year_published" in data:
        book.year_published = data["year_published"]
    if "book_type" in data:
        book.book_type = data["book_type"]

    db.session.commit()

    return jsonify({"message": "Book updated successfully"})

@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({"message": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully"})