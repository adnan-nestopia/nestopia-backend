from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory room data (temporary until we connect MongoDB)
rooms = [
    {"id": 1, "name": "Ocean View Suite", "price_per_night": 120, "available": True},
    {"id": 2, "name": "Garden Room", "price_per_night": 90, "available": True},
    {"id": 3, "name": "Mountain Cabin", "price_per_night": 150, "available": True},
]

@app.route('/')
def home():
    return '🏡 Welcome to Nestopia! Your homestay backend is live.'

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms)

@app.route('/book', methods=['POST'])
def book_room():
    data = request.get_json()
    room_id = data.get("room_id")
    guest_name = data.get("guest_name")

    for room in rooms:
        if room["id"] == room_id:
            if room["available"]:
                room["available"] = False
                return jsonify({
                    "message": f"Room {room['name']} has been booked by {guest_name}."
                }), 200
            else:
                return jsonify({"error": "Room is not available"}), 400

    return jsonify({"error": "Room not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
