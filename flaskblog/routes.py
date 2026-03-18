from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required

from flaskblog import app, bcrypt, db

from .forms import LoginForm, RegistrationForm
from .models import Post, User

posts = [
    {
        'author': 'Denys',
        'title': 'Pizdabol',
        'content': 'Pizdabol is a big lier.',
        'date_posted': '23-05-2026',
    },
    {
        'author': 'Pizdabol',
        'title': 'Denys is a liar',
        'content': 'Denys is a liar, Im not a lier.',
        'date_posted': '24-05-2026',
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()

        if user and bcrypt.check_password_hash(
            user.password, login_form.password.data
        ):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('home'))

        else:
            flash(
                'Login unsuccessful. Please check your email and password.',
                'danger',
            )

        return redirect(url_for('login'))
    return render_template('login.html', form=login_form, title='Login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            registration_form.password.data
        ).decode('utf-8')
        new_user = User(
            username=registration_form.username.data,
            email=registration_form.email.data,
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()

        flash(
            'Your account has been created! You are now able to log in.',
            'success',
        )
        return redirect(url_for('login'))

    return render_template(
        'register.html', form=registration_form, title='Register'
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
    
