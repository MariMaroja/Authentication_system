from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creates the Flask application
app = Flask(__name__)
# Configures the application's database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creates the database instance
db = SQLAlchemy(app)