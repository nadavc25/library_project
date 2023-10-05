const apiUrl = 'http://127.0.0.1:5000';  // Replace with your actual API endpoint
let books = [];

const fetchBooks = async () => {
    try {
        const response = await axios.get(`${apiUrl}/books`);
        books = response.data;
        displayBooks(books);
    } catch (error) {
        console.error('Error fetching books:', error);
    }
};

const displayBooks = (books) => {
    const booksTableBody = document.getElementById('books-table-body');
    booksTableBody.innerHTML = '';

    books.forEach(book => {
        const typeMapping = {
            1: 'up to 10 days loan',
            2: 'up to 5 days loan',
            3: 'up to 2 days loan'
        };

        const row = `
    <tr>
        <td>${book.id}</td>
        <td>${book.name}</td>
        <td>${book.author}</td>
        <td>${book.year_published}</td>
        <td>${typeMapping[book.book_type]}</td>
        <td>${book.quantity}</td>
        <td>
            <button class="btn btn-danger btn-sm" onclick="deleteBook(${book.id})">Delete</button>
            <button class="btn btn-primary btn-sm ml-2" onclick="editBook(${book.id})">Edit</button>
        </td>
    </tr>
`;
        booksTableBody.innerHTML += row;
    });
};


const searchBooks = () => {
    const searchOption = document.getElementById('searchOption').value;
    const searchText = document.getElementById('searchBox').value.toLowerCase();

    if (!searchText.trim()) {
        // If the search box is empty, display all books
        displayBooks(books);
        return;
    }

    const filteredBooks = books.filter(book => {
        const fieldValue = book[searchOption];

        if (typeof fieldValue === 'number' || typeof fieldValue === 'string') {
            const fieldString = fieldValue.toString().toLowerCase();
            return fieldString.startsWith(searchText);
        }

        return fieldValue === searchText;
    });

    displayBooks(filteredBooks);
};

const addBook = (event) => {
    event.preventDefault();

    const name = document.getElementById('addName').value;
    const author = document.getElementById('addAuthor').value;
    const yearPublished = document.getElementById('addYear').value;
    const bookType = document.getElementById('addType').value;

    axios.post(`${apiUrl}/books`, {
        name,
        author,
        year_published: yearPublished,
        book_type: bookType
    })
        .then(response => {
            fetchBooks(); // Refresh the book list after adding
            $('#addModal').modal('hide');
        })
        .catch(error => console.error('Error adding book:', error));
};


const deleteBook = (bookId) => {
    // Display confirmation dialog
    const isConfirmed = window.confirm("Are you sure you want to delete this book?");

    // Check if the user confirmed
    if (isConfirmed) {
        axios.delete(`${apiUrl}/books/${bookId}`)
            .then(response => fetchBooks())
            .catch(error => console.error('Error deleting book:', error));
    }
};


const editBook = (bookId) => {
    const book = books.find(b => b.id === bookId);
    document.getElementById('editBookId').value = book.id;
    document.getElementById('editName').value = book.name;
    document.getElementById('editAuthor').value = book.author;
    document.getElementById('editYear').value = book.year_published;
    document.getElementById('editType').value = book.book_type;
    $('#editModal').modal('show');
};
const saveChanges = () => {
    const bookId = document.getElementById('editBookId').value;
    const name = document.getElementById('editName').value;
    const author = document.getElementById('editAuthor').value;
    const yearPublished = document.getElementById('editYear').value;
    const bookType = document.getElementById('editType').value;
    
    axios.put(`${apiUrl}/books/${bookId}`, {
        name,
        author,
        
        year_published: yearPublished,
        book_type: bookType
    })
    .then(response => {
        fetchBooks();
        $('#editModal').modal('hide');
    })
    .catch(error => console.error('Error updating book:', error));
};


document.getElementById('addBookForm').addEventListener('submit', addBook);

// Initial fetch of books when the page loads

fetchBooks();
