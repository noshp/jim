from . import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(128), index=True, unique=False)
    date = db.Column(db.DateTime, nullable=True, unique=False)
