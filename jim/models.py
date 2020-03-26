from . import db
from sqlalchemy.dialects.postgresql import JSON

class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(128), index=True, unique=False)
    date = db.Column(db.DateTime, nullable=True, unique=False)

class ArchiveStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, unique=False)
    stats = db.Column(JSON)