from . import db
from flask_login import UserMixin
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
    #Relationship
    expenses = db.relationship('Expense', backref='owner')
    comments = db.relationship('Comment', backref='owner')

    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



class Expense(db.Model):
    __tablename__= 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    merchant = db.Column(db.String(), index=True) 
    amount = db.Column(db.Integer)
    description = db.Column(db.String(), index=True)

    def __repr__(self):
            return f'Expense {self.description}' 


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(255), index=True)
   
 
    def __repr__(self):
            return f'Comment {self.content}'   
