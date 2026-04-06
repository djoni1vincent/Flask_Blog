from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
)

# from flaskblog.models import Item


class SearchForm(FlaskForm):
    ids = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')
