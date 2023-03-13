from libs.conf import *
from flask_login import UserMixin

class TblUsers (db.Model, UserMixin):
    __tablename__ = 'TblUsers'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<TblUsers {self.id}>"