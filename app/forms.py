from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class CustomerRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password_hash = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password_hash')])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    firstname = StringField("First Name", validators=[DataRequired(), Length(min=2)])
    lastname = StringField("Last Name", validators=[DataRequired(), Length(min=2)])
    dob = DateField('Birthday')
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    zip = StringField('Zip Code', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Save')


class CustomerLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')


class EmployeeAddForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user_role = SelectField('Role', validators=[DataRequired()], choices=[('administrator', "Administrator"), ('moderator', "Moderator"), ('user', "User")])


class EmployeeLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=0, max=100)])
