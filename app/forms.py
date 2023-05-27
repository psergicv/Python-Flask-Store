from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class CustomerRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    firstname = StringField("First Name", validators=[DataRequired(), Length(min=2)])
    lastname = StringField("Last Name", validators=[DataRequired(), Length(min=2)])
    dob = DateField('Birthday')
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    zip = StringField('Zip Code', validators=[DataRequired])
    phone = StringField('Phone Number', validators=[DataRequired()])


class CustomerLoginForm(FlaskForm):
    pass


class EmployeeAddForm(FlaskForm):
    pass


class EmployeeLoginForm(FlaskForm):
    pass
