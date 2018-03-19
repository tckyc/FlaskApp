from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # e_mail=StringField('What is your e-mail?',validators=[DataRequired()])
    submit = SubmitField('确定')
