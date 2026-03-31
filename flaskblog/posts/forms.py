from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
)


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = PageDownField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
