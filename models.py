import pymysql
from app import app, db

# Makes PyMySQL behave like MySQLdb
pymysql.install_as_MySQLdb()

# Creates the User table in the database
class User(db.Model):
    # Unique ID for each user (Primary Key)
    id = db.Column(db.Integer, primary_key=True)
    # Username field, must be unique and cannot be null
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Password field, cannot be null
    password = db.Column(db.String(200), nullable=False)

    # Defines how the object will appear when printed
    def __repr__(self):
        return f'<User {self.username}>'
    
# Creates the Rose table in the database
class Rose(db.Model):
    # Unique ID for each rose (Primary Key)
    id = db.Column(db.Integer, primary_key=True)
    # Name field, must be unique and cannot be null
    name = db.Column(db.String(80), unique=True, nullable=False)
    # Description field, cannot be null
    description = db.Column(db.Text, nullable=False)

    # Defines how the object will appear when printed
    def __repr__(self):
        return f'<Rose {self.name}>'
    
# Creates the Peony table in the database
class Peony(db.Model):
    # Unique ID for each peony (Primary Key)
    id = db.Column(db.Integer, primary_key=True)
    # Name field, must be unique and cannot be null
    name = db.Column(db.String(80), unique=True, nullable=False)
    # Description field, cannot be null
    description = db.Column(db.Text, nullable=False)

    # Defines how the object will appear when printed
    def __repr__(self):
        return f'<Peony {self.name}>'