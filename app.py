from flask import Flask, jsonify, request

app = Flask(__name__)

# Room data: 8 simple rooms
rooms = [
    {"id": 1, "price": 120, "available": True},
    {"id": 2, "price": 180, "available": True},
    {"id": 3, "price": 90, "available": True},
    {"id": 4, "price": 200, "available": True},
    {"id": 5, "price": 150, "available": True},
    {"id": 6, "price": 110, "available": True},
    {"id": 7, "price": 135, "available": True},
    {"id": 8, "price": 100, "available": True}
]

# In-memory booking and contact storage
bookings = []
messages = []

@app.route('/')
def home():
    return '🏡 Welcome to Nestopia! Your homestay backend is live.'

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify({"rooms": rooms})

@app.route('/book', methods=['POST'])
def book_room():
    data = request.json
    room_id = data.get("room_id")
    guest_name = data.get("guest_name")
    checkin = data.get("checkin_date")
    checkout = data.get("checkout_date")

    for room in rooms:
        if room["id"] == room_id:
            if room["available"]:
                room["available"] = False
                booking = {
                    "room_id": room_id,
                    "guest_name": guest_name,
                    "checkin_date": checkin,
                    "checkout_date": checkout
                }
                bookings.append(booking)
                return jsonify({"message": "Booking successful!", "booking": booking}), 200
            else:
                return jsonify({"error": "Room is already booked"}), 400

    return jsonify({"error": "Room not found"}), 404

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    messages.append(data)
    return jsonify({"message": "Thank you for contacting us!", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
