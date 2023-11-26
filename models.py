from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserLogin(db.Model):
    __tablename__ = 'user_login'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(30), nullable=True)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issue_description = db.Column(db.Text, nullable=True)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user_login.id'), nullable=True)
    raised_by = db.Column(db.Integer, db.ForeignKey('user_login.id'), nullable=True)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=True)
