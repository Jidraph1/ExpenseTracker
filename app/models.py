from . import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
    #relationship
    expense_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.username}'


class Expense(db.Model):
    __tablename__= 'expenses'
    id = db.Column(bd.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    merchant = db.Column(db.String) 
    amount = db.Column(bd.Integer)
    users = db.relationship('User', backref = 'expenses', lazy='dynamic')
    description = db.Column(db.String)