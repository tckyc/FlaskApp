from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from  ..models import Role,User


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # e_mail=StringField('What is your e-mail?',validators=[DataRequired()])
    submit = SubmitField('确定')


class EditProfileForm(FlaskForm):
    name = StringField('暱稱', validators=[Length(0, 64)])
    location = StringField('居住地', validators=[Length(0, 64)])
    about_me = TextAreaField('簡介')
    submit = SubmitField('確認')


class EditProfileAdminForm(FlaskForm):
    email = StringField('郵箱', validators=[DataRequired(), Length(1, 64),
                        Email()])
    username = StringField('用戶名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               '用戶名只能包含數字字母下劃線')])
    confirmed = BooleanField('記住密碼')
    role = SelectField('用戶組', coerce=int)
    name = StringField('暱稱', validators=[Length(0, 64)])
    location = StringField('居住地', validators=[Length(0, 64)])
    about_me = TextAreaField('簡介')
    submit = SubmitField('確認')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm,self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('郵件已註冊！')

    def validate_username(self,field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用戶名已註冊！')


