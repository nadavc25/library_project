# Library Management System

The Library Management System is a web application built with Flask and JavaScript for managing books and customers in a library. It allows library administrators to add, edit, and delete books, add, edit, and delete customers, and manage loans.

## Features

- **Books Management:**
  - Add books with details like title, author, publication year, and book type.
  - Edit book details.
  - Delete books from the library.

- **Customers Management:**
  - Add customers with details like name, city, and age.
  - Edit customer details.
  - Delete customers from the database.

- **Loan Management:**
  - Loan books to customers.
  - Return books and update return dates.

- **Search Functionality:**
  - Search for books and customers based on different criteria.

## Technologies Used

- **Frontend:**
  - HTML, CSS, Bootstrap
  - JavaScript (axios, jQuery)
  
- **Backend:**
  - Python (Flask)
  - SQLAlchemy (Database ORM)
  
- **Database:**
  - SQLite (Can be upgraded to other databases)

## Getting Started

1. Clone this repository to your local machine. ``
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. Open a web browser and navigate to `http://localhost:5000` to access the Library Management System.

## Usage

- **Books Management:**
  - Click on the "Add Book" button to add a new book.
  - Click on "Edit" to edit book details.
  - Click on "Delete" to remove a book from the library.

- **Customers Management:**
  - Click on the "Add Customer" button to add a new customer.
  - Click on "Edit" to edit customer details.
  - Click on "Delete" to remove a customer from the database.

- **Loan Management:**
  - To loan a book to a customer, select a customer and a book, and click "Loan Book".
  - To return a book, click the "Return Loan" button.

## Contributors

- [Your Name](https://github.com/your-username)

## License

This project is open-source and available under the [MIT License](LICENSE).
