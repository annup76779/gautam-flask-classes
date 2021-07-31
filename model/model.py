from enum import unique
from wsgi import db
from datetime import datetime
from passlib.hash import sha256_crypt


class User(db.Model):
    __tablename__ = "myappusers"

    """id INT(5) PRIMARY KEY AUTOINCREMENT,
        user_email VARCHAR(200) NOT NULL,
        password VARCHAR(38) NOT NULL
    """

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_email = db.Column(db.String(200), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)
    data_created = db.Column(db.DateTime, nullable=False, default = datetime.now())

    def hash_password(self, password):
        self.password = sha256_crypt.hash(password)

    def verify_password(self, password):
        return sha256_crypt.verify(password, self.password)