from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    ValidationError,
)

from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = StringField(
        'Email', validators=[Email(), DataRequired(), Length(min=5, max=90)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=2, max=40)]
    )
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.'
            )

    def validate_email(self, email):
        existing_email = User.query.filter_by(email=email.data).first()
        if existing_email:
            raise ValidationError(
                'That email is taken. Please choose a different one.'
            )


class LoginForm(FlaskForm):
    email = StringField(
        'Email', validators=[Email(), DataRequired(), Length(min=5, max=50)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=2, max=40)]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
