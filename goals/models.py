from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

from .goals import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime())
    last_login = db.Column(db.DateTime())

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.username