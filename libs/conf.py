from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:19982804@localhost:3306/TblUsers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "59ceec65a970fa3b1a00830e53081eb6f565c272"
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

