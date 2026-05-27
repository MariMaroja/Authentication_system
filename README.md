# Authentication_system

This is a Flask web application designed to organize and display flower information in a simple and intuitive way.

The project allows users to register, log in, and explore flower collections such as roses and peonies. Authenticated users can also add new flowers to the collection.

This project was created to practice authentication systems, database management, and backend development using Flask.

## Features

- User registration
- User login and logout
- Session-based authentication
- View rose collection
- View peony collection
- Add new flowers (authenticated users only)
- Database integration with SQLAlchemy
- Simple UI using HTML and CSS

## Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Bcrypt (password hashing)

### Frontend
- HTML
- CSS

## Project Structure

```txt
FlowerVault/
│
├── static/
│   └── css/
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── roses.html
│   ├── peonies.html
│   ├── add_rose.html
│   └── add_peony.html
│
├── models.py
├── routes.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd FlowerVault
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

The application will be available at:

```txt
http://127.0.0.1:5000
```

## Database

This project uses SQLite with SQLAlchemy ORM.

The database file is automatically created as:

```txt
site.db
```

Example configuration:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
```

## Authentication System

The authentication system includes:

- User registration
- Password hashing
- Login system
- Logout functionality
- Session management
- Protected routes for authenticated users

## Learning Goals

This project was built to practice:

- Flask fundamentals
- Authentication systems
- Session management
- Database modeling with SQLAlchemy
- CRUD operations
- HTML template rendering
- Backend and frontend integration

## Future Improvements

- Flower images
- Search functionality
- Edit and delete flowers
- User profile system
- Better UI/UX design
- Categories and tags
- Pagination

## Screenshots

Coming soon.

## License

This project is for educational and portfolio purposes.
