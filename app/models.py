from . import db
from . import login_manager

class Users(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
    #relationship
    # expense_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))



# class Expense(db.Model):
#     __tablename__= 'expenses'
#     id = db.Column(bd.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True, nullable=False)
#     merchant = db.Column(db.String) 
#     amount = db.Column(bd.Integer)
#     users = db.relationship('User', backref = 'expenses', lazy='dynamic')
#     description = db.Column(db.String)

    # def __repr__(self):
    #         return f'Pitch {self.description}' 
