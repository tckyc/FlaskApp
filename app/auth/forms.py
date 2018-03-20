from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email,Regexp,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('郵箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密碼', validators=[DataRequired()])
    remember_me = BooleanField('記住密碼')
    submit = SubmitField('登錄')


class RegistrationForm(FlaskForm):
    email = StringField('郵箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('用戶名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               '用戶名只能包含數字字母下劃線')])
    password = PasswordField('密碼', validators=[DataRequired()])
    password2 = PasswordField('確認密碼', validators=[DataRequired(),
                        EqualTo('password', message='密碼必須一致')])
    submit = SubmitField('登錄')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('郵箱已被註冊')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用戶名已被註冊')
