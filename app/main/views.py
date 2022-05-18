from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from .forms import LoginForm, RegisterForm
from ..models import User, Expense, Comment
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from . import main
from .. import db


#Views 
@main.route('/')
def index():
    """ View root page that returns the index page and its data
    """
    title = "Welcome to home page"
    return render_template('index.html', title = title)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
       
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    
        db.session.add(new_user)
        db.session.commit()
        return redirect('/success')
    return render_template('signup.html', form=form)

@main.route('/success')
def success():
    return render_template("success.html")

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.success'))
         
        return redirect('failure')
    
  
    return render_template('login.html', form=form )

@main.route('/failure')
def failure():
    
    return render_template('failure.html')

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    expense = Expense.query.all()
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(owner_id=current_user.id, content=form.content.data)
        form.content.data = ''
       
        
        db.session.add(comment)
        db.session.commit()
    return render_template('dashboard.html', name=current_user.username, expense=expense, form=form, content=form.content.data)

@main.route('/expense', methods=['GET', 'POST'])
@login_required
def expense():
    form = ExpenseForm()
    
    if form.validate_on_submit():
        expense = Expense(owner_id=current_user.id, name=form.name.data, merchant=form.merchant.data, amount=form.amount.data, description=form.description.data)
        form.name.data = ''
        form.merchant.data = ''
        form.amount.data = ''
        form.description.data = ''
        
        db.session.add(expense)
        db.session.commit()
    return render_template('expense.html', form=form)

@main.route('/profile')
@login_required
def profile():
    
    expense = Expense.query.filter_by(id=current_user.id).all()
    
    return render_template('profile.html', name=current_user.username, email=current_user.email, password=current_user.password, expense=expense)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    
# from . import auth
# from .. import db
# from flask import render_template, request, flash, redirect, url_for
# from ..models import User
# from werkzeug.security import generate_password_hash, check_password_hash
# # from .email import mail_message
# from flask_login import login_user, login_required, current_user


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 flash('Logged in successfully', category='success')
#                 login_user(user)
#                 return redirect(url_for('main.index'))
#             else:
#                 flash('You entered wrong email or password', category='error')
#         else:
#             flash('Email does not exist.', category='error')
#     return render_template("templates/login.html", user=current_user)


# @auth.route('/sign-up', methods=["GET", "POST"])
# def sign_up():
#      if request.method == 'POST':
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('A user with this email already exists', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 4 characters.', category='error')
#         elif len(username) < 2:
#             flash('Pick a username that is greater than 2 characters.', category='error')
#         elif len(password1) < 7:
#             flash('Use a stronger password that is more than 7 characters long.', category='error')
#         elif password1 != password2:
#             flash('Passwords did not match!!!', category='error')
#         else:
#             # create a new user if form is valid
#             new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
#             # add the new user to our db
#             db.session.add(new_user)
#             db.session.commit()
#             # send welcome email to new user
#             #
#             flash('Account created successfully.', category='success')
#             return redirect(url_for('templates.login'))
#      return render_template("templates/sign-up.html", user=current_user) 
# >>>>>>> 9725e40f49cfa8f9965db316efe76030e99abf36
