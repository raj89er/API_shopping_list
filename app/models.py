
from . import db
from datetime import datetime, timezone

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date_added = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

