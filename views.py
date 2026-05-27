import bcrypt
from flask import render_template, request, redirect, session, flash, url_for
from models import User, Rose, Peony
from app import app, db

# Home page route
@app.route('/')
def index():
    # Renders the home page
    return render_template('index.html')

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Gets JSON data sent in the request
    data = request.json

    # Extracts username and password
    username = data.get('username')
    password = data.get('password')

    # Checks if required fields are empty
    if not username or not password:
        return {'message': 'Username and password are required'}, 400
    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:   
        return {'message': 'Username already exists'}, 400
    
    # Checks if the username already exists
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Creates a new user object
    user = User(username=username, password=hashed_password)

    # Saves the user to the database
    db.session.add(user)
    db.session.commit()
    # Shows a success message
    flash('Registration successful! Please log in.')
    # Renders the register page again
    return render_template('register.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Checks if the user is already logged in
    if 'user_id' in session:
        # Redirects logged users to home page
        return redirect(url_for('index'))
    else:
        # Gets the "next" parameter
        next = request.args.get('next')
        return render_template('login.html', next=next)

# Logout route
@app.route('/logout')
def logout():
    # Removes logged user session
    session['user_id'] = None
    # Shows logout success message
    flash('You have been logged out.')
    # Redirects to home page
    return redirect(url_for('index'))

# Authentication route
@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Finds the user by username
    user = User.query.filter_by(username=request.form['username']).first()
    # Verifies username and password
    if user and user.password == request.form['password']:
        # Stores user ID in session
        session['user_id'] = user.id
        # Shows success message
        flash('Login successful!')
        # Redirects user to previous page or home page
        next = request.form.get('next')
        return redirect(next or url_for('index'))
    else:
        # Shows login error message
        flash('Invalid username or password')
        # Redirects back to login page
        return redirect(url_for('login'))

# Displays all roses
@app.route('/roses')
def roses():
    # Retrieves all roses from database
    rose = Rose.query.all()
    # Renders roses page with retrieved roses
    return render_template('roses.html', rose=rose)

# Adds a new rose
@app.route('/add_rose', methods=['POST'])
def add_rose():
    # Checks if user is logged in
    if 'user_id' in session:
        # Gets form data
        name = request.form['name']
        description = request.form['description']

        # Creates rose if data exists
        if name and description:
            rose = Rose(name=name, description=description)
            db.session.add(rose)
            db.session.commit()
        # Redirects to roses page;  Renders add rose page
        return render_template('add_rose.html'); return redirect(url_for('roses'))

    else:
        # Redirects unauthenticated users to login page
        return redirect(url_for('login'))

# Displays all peonies
@app.route('/peonies')
def peonies():
    # Retrieves all peonies from database
    peony = Peony.query.all()
    # Renders peonies page with retrieved peonies
    return render_template('peonies.html', peony=peony)

# Adds a new peony
@app.route('/add_peony', methods=['POST'])
def add_peony():
    # Checks if user is logged in
    if 'user_id' in session:
        # Gets form data
        name = request.form['name']
        description = request.form['description']

        # Creates peony if data exists
        if name and description:
            peony = Peony(name=name, description=description)
            db.session.add(peony)
            db.session.commit()
        # Redirects to peonies page; Renders add peony page
        return render_template('add_peony.html'); return redirect(url_for('peonies'))
    else:
        # Redirects unauthenticated users
        return redirect(url_for('login'))