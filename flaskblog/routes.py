import os
import secrets

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required
from PIL import Image
from sqlalchemy.sql.functions import random

from flaskblog import app, bcrypt, db

from .forms import LoginForm, PostForm, RegistrationForm, UpdateAccountForm
from .models import Post, User


@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
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
        user = User.query.filter(
            (User.email == login_form.login.data)
            | (User.username == login_form.login.data)
        ).first()
        if user and bcrypt.check_password_hash(
            user.password, login_form.password.data
        ):
            next_page = request.args.get('next')
            login_user(user, remember=login_form.remember.data)
            return redirect(next_page or url_for('home'))

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


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn
    )

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file
    )

    return render_template(
        'account.html', title='Account', image_file=image_file, form=form
    )


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))

    return render_template('create_post.html', title='New Post', form=form)
