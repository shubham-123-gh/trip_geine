from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS once
#from flask import Flask, request, jsonify
from flask import request
from scraping import get_hotels_data

app = Flask(_name_)
CORS(app)  # Enable CORS for frontend-backend communication

# Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to Trip Genie Backend"})
# Scraping Route
@app.route("/scrape_hotels", methods=["GET"])
def scrape_hotels():
    hotel_data = get_hotels_data()  # Call the scraping function
    if hotel_data:
        return jsonify(hotel_data)  # Send the scraped data as a JSON response
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500
# Destinations Route
@app.route("/destinations")
def destinations():
    data = [
        {"name": "Kolkata", "country": "India"},
        {"name": "Darjeeling", "country": "India"},
        {"name": "Varanasi", "country": "India"},
        {"name": "Mumbai", "country": "India"},
        {"name": "Tokyo", "country": "Japan"}
    ]
    return jsonify(data)

# Flights Route
@app.route("/flights")
def flights():
    data = [
        {"airline": "Air India", "from": "Delhi", "to": "London", "price": "$500"},
        {"airline": "Emirates", "from": "Dubai", "to": "New York", "price": "$700"}
    ]
    return jsonify(data)

# Train Tickets Route
@app.route("/trains")
def trains():
    data = [
        {"train": "Rajdhani Express", "from": "Delhi", "to": "Mumbai", "price": "$40"},
        {"train": "Shatabdi Express", "from": "Chennai", "to": "Bangalore", "price": "$20"}
    ]
    return jsonify(data)

# Bus Tickets Route
@app.route("/buses")
def buses():
    data = [
        {"bus": "Volvo AC", "from": "Pune", "to": "Goa", "price": "$15"},
        {"bus": "Sleeper Coach", "from": "Hyderabad", "to": "Bangalore", "price": "$10"}
    ]
    return jsonify(data)

# Budget Estimation Route
@app.route("/budget")
def budget():
    data = {
        "flights": 500,
        "hotels": 300,
        "food": 200,
        "transport": 100,
        "total": 1100
    }
    return jsonify(data)

# Preferences Route
@app.route("/preferences")
def preferences():
    data = {
        "preferred_transport": "Flights",
        "preferred_budget": "Mid-Range",
        "preferred_destination_type": "Beach"
    }
    return jsonify(data)

# Destination Search API
@app.route("/api/search/<destination>", methods=["GET"])
def search(destination):
    results = [
        {"id": 1, "name": "Kolkata", "description": "City of Joy"},
        {"id": 2, "name": "Darjeeling", "description": "City of Tea"},
        {"id": 3, "name": "Banaras", "description": "City of Ghats"},
        {"id": 4, "name": "Mumbai", "description": "City of Dreams"},
        {"id": 5, "name": "Delhi", "description": "Capital City"},
        {"id": 6, "name": "Goa", "description": "Beach Paradise"},
        {"id": 7, "name": "Jaipur", "description": "Pink City"},
        {"id": 8, "name": "Agra", "description": "City of Taj Mahal"},
        {"id": 9, "name": "Kerala", "description": "God's Own Country"},
        {"id": 10, "name": "Ladakh", "description": "Land of High Passes"},
        {"id": 11, "name": "Andaman", "description": "Island Paradise"},
        {"id": 12, "name": "Rajasthan", "description": "Land of Kings"},
        {"id": 13, "name": "Himachal Pradesh", "description": "Abode of Snow"},
        {"id": 14, "name": "Sikkim", "description": "Land of Monasteries"},
        {"id": 15, "name": "Uttarakhand", "description": "Land of Gods"},
        {"id": 16, "name": "Mysore", "description": "City of Palaces"},
        {"id": 17, "name": "Pondicherry", "description": "French Riviera of the East"},
        {"id": 18, "name": "Coorg", "description": "Scotland of India"},
        {"id": 19, "name": "Rishikesh", "description": "Yoga Capital of the World"},
    ]
    filtered_results = [item for item in results if destination.lower() in item["name"].lower()]
    return jsonify(filtered_results)
    

# Booking API
@app.route("/api/bookings", methods=["GET"])
def get_bookings():
    bookings = [
        {"id": 101, "type": "Flight", "destination": "Paris"},
        {"id": 102, "type": "Hotel", "destination": "Tokyo"}
    ]
    return jsonify(bookings)

destination_data = {
    "Paris": {
        "hotels": ["Hotel Ritz", "Le Meurice", "Shangri-La Hotel"],
        "restaurants": ["Le Jules Verne", "L'Ambroisie", "Epicure"],
        "cuisines": ["French", "Pastries", "Wine"],
        "places": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"]
    },
    "New York": {
        "hotels": ["The Plaza", "The Ritz-Carlton", "Four Seasons"],
        "restaurants": ["Le Bernardin", "Per Se", "Gramercy Tavern"],
        "cuisines": ["American", "Steakhouse", "Pizza"],
        "places": ["Statue of Liberty", "Central Park", "Times Square"]
    }
}
@app.route('/destination/details')
def get_destination_details():
    destination_name = request.args.get("name")
    details = destination_data.get(destination_name, {})
    return jsonify(details)
@app.route('/destination/<int:destination_id>', methods=['GET'])
def get_destination_by_id(destination_id):
    # Example data - Replace with database fetch logic
    destinations_data = {
        1: {
            "name": "Paris",
            "description": "The city of lights!",
            "hotels": ["Hotel A", "Hotel B"],
            "restaurants": ["Restaurant X", "Restaurant Y"],
            "places": ["Eiffel Tower", "Louvre Museum"]
        },
        2: {
            "name": "New York",
            "description": "The Big Apple!",
            "hotels": ["NY Hotel 1", "NY Hotel 2"],
            "restaurants": ["Diner Z", "Bistro W"],
            "places": ["Statue of Liberty", "Times Square"]
        }
    }

    destination = destinations_data.get(destination_id, None)
    if destination:
        return jsonify(destination)
    else:
        return jsonify({"error": "Destination not found"}), 404

# Preferences API
@app.route("/api/preferences", methods=["GET"])
def get_preferences():
    preferences = {"preferred_transport": "Flight", "budget": "Mid-range"}
    return jsonify(preferences)

if _name_ == "_main_":
    app.run(debug=True)  # Runs on default port 5000
#from waitress import serve
#from app import app

#if _name_ == "_main_":
    #serve(app, host='0.0.0.0', port=5000)
# This will run the Flask app using Waitress server
