from flask import Flask, jsonify, request
from models import db, Room, Booking

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nestopia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    if Room.query.count() == 0:
        for i in range(1, 9):
            db.session.add(Room(id=i))
        db.session.commit()

@app.route('/')
def home():
    return "🏡 Welcome to Nestopia! Your homestay backend is live."

@app.route('/rooms')
def rooms():
    rooms = Room.query.all()
    return jsonify([{'room_id': r.id, 'booked': r.booked} for r in rooms])

@app.route('/book', methods=['POST'])
def book():
    data = request.get_json()
    room = Room.query.get(data['room_id'])
    if room and not room.booked:
        room.booked = True
        booking = Booking(
            room_id=room.id,
            guest_name=data['guest_name'],
            checkin_date=data['checkin_date'],
            checkout_date=data['checkout_date']
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify({'message': 'Booking successful'})
    return jsonify({'message': 'Room is already booked or not found'}), 400
