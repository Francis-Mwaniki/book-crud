
```markdown
# Django CRUD Book App

This is a simple Django web application that allows you to perform CRUD (Create, Read, Update, Delete) operations on books. The application provides a user-friendly interface for managing a book list, adding new books, updating existing books, and deleting books.

## Features

- List all available books
- Create a new book
- Update book details
- Delete a book

## Technologies Used

- Python 3.10
- Django 5.0.4
- HTML
- CSS

## Getting Started

Follow these steps to set up and run the project on your local machine:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

```sh
git clone git@github.com:Francis-Mwaniki/book-crud.git
```

2. Navigate to the project directory:

```sh
cd django-crud-book-app
```

3. Create a virtual environment and activate it:

```sh
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

4. Install the required dependencies:

```sh
pip install -r requirements.txt
```

5. Apply the database migrations:

```sh
python manage.py migrate
```

### Usage

1. Start the development server:

```sh
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000` to access the application.

### Demo

Here are some screenshots showcasing the application's user interface:

![Book List](screenshots/book_list.png)
![Create Book](screenshots/create_book.png)
![Update Book](screenshots/update_book.png)
![Delete Book](screenshots/delete_book.png)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

