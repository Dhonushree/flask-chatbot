"""Database model for storing chat logs."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(512))
    response = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
