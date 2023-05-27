from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Customer(db.Model):
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(75), nullable=False)
    lastname = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(75), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    zip = db.Column(db.String(30), nullable=False)

    orders = db.relationship('Order', backref='customer', lazy='dynamic')
    cart = db.relationship('Cart', backref='customer', lazy='dynamic')

    def __repr__(self):
        return f"{self.id} - {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(75), unique=True, nullable=False)
    firstname = db.Column(db.String(75), nullable=False)
    lastname = db.Column(db.String(75), nullable=False)
    user_role = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.username} - {self.user_role}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_description = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    stock_qty = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String)
    category = db.Column(db.String)

    def __repr__(self):
        return f"{self.id} - {self.product_name}"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Order(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='New')

    customer = db.relationship('Customer', backref='orders')
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')

    def __repr__(self):
        return f"{self.id} - {self.status}"

    def save(self):
        db.session.add(self)
        db.session.commit()


class OrderItem(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_at_purchase = db.Column(db.Float, nullable=False)

    product = db.relationship('Product', backref='order_items')

    def __repr__(self):
        return f"OrderItem {self.id} for Order {self.order_id}"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Cart(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    customer = db.relationship('Customer', backref='cart')
    product = db.relationship('Product', backref='cart_items')

    def __repr__(self):
        return f"Cart {self.id}"
