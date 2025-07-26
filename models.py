from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booked = db.Column(db.Boolean, default=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    guest_name = db.Column(db.String(100), nullable=False)
    checkin_date = db.Column(db.String(20), nullable=False)
    checkout_date = db.Column(db.String(20), nullable=False)
