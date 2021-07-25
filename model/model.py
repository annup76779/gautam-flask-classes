from wsgi import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "myappusers"

    """id INT(5) PRIMARY KEY AUTOINCREMENT,
        user_email VARCHAR(200) NOT NULL,
        password VARCHAR(38) NOT NULL
    """

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(38), nullable = False)
    data_created = db.Column(db.DateTime, nullable=False, default = datetime.now())