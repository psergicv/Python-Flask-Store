from app import db


class Client(db.Model):
    id = db.Column(db.Integer(), unique=True, foreign_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(36), unique=True, nullable=False)
    firstname = db.Column(db.String(75), unique=True, nullable=False)
    lastname = db.Column(db.String(75), unique=True, nullable=False)
    email = db.Column(db.String(75), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    zip = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer(), unique=True, foreign_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(36), unique=True, nullable=False)
    email = db.Column(db.String(75), unique=True, nullable=False)
    firstname = db.Column(db.String(75), nullable=False)
    lastname = db.Column(db.String(75), nullable=False)
    user_role = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.username} - {self.user_role}"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Product(db.Model):
    pass


class Order(db.Model):
    pass


class Cart(db.Model):
    pass
