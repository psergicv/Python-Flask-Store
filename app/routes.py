from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user
from urllib.parse import urlsplit
from .models import Customer
from .forms import CustomerRegisterForm, CustomerLoginForm
from app import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


@app.route("/")
def index():
    return render_template("user_side_html/index.html")


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        customer = Customer(
            username=form.username.data,
            password_hash=form.password_hash.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            dob=form.dob.data,
            country=form.country.data,
            city=form.city.data,
            street=form.street.data,
            zip=form.zip.data,
            phone=form.phone.data
        )
        customer.set_password(form.password_hash.data)
        db.session.add(customer)
        db.session.commit()
        return "Registered!"
    return render_template("user_side_html/register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated:  # if the user is already logged in
        return redirect(url_for('index'))  # redirect them to home page

    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user_login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template("user_side_html/login.html", form=form)


# ================================= Employee Side =========================

@app.route('/internal/login')
def employee_login():
    return render_template('admin_side_html/login.html')
