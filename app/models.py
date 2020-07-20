from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=True)
    color = db.Column(db.String(64), index=True, nullable=True)
    pet = db.Column(db.String(64), index=True, nullable=True)