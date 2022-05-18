from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm, form
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea
from wtforms import ValidationError

ogin registration form
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember')

#  SignUp Registration form
class RegisterForm(FlaskForm):
    
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('username',validators=[InputRequired()])   
    password = PasswordField('Password',validators=[InputRequired()])


    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')