from flask_wtf import FlaskForm
from wtforms import SteingField, PasswordField, BooleanField
from wtforms.widgets import TestArea
from wtforms.validators import InputRequired, Email

# class LoginForm(FlaskForm):
#     username = StringField('Username',validators=[InputRequired()])
#     password = PasswordField('Password',validators=[InputRequired()])
#     remember = BooleanField('Remember')
    
# class RegisterForm(FlaskForm):
#     email = StringField('Email', valdators=[InputRequired(), Email()])
#     username = StringField('username',validators=[InputRequired()])
#     password = StringField('password', validators=[InputRequired()])
