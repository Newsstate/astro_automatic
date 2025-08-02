from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from panchang.calculator import calculate_panchang
from panchang.ekadashi import find_ekadashis
from datetime import datetime, date
from panchang.festivals import calculate_festivals
from panchang.festival_calculator import calculate_festival_days
from datetime import date


# Initialize the Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# Root route to serve the index.html
@app.route("/")
def show_panchang_page():
    return render_template("index.html")  # Render the index.html from the templates folder

# Function to generate slug from festival name
def generate_slug(festival_name):
    return festival_name.lower().replace(" ", "-").replace(",", "").replace(".", "")

# Modify this function to fetch festivals dynamically
def get_festival_by_slug(slug, festival_date):
    # Calculate festivals dynamically
    all_festivals = calculate_festival_days(date(2024, 1, 1), date(2024, 12, 31))  # Adjust date range as needed
    
    # Match festival by both slug (festival name) and date
    festival = next((f for f in all_festivals if generate_slug(f['name']) == slug and f['date'] == festival_date), None)

    return festival

# Route for festival details page
@app.route("/<slug>-date-time")
def festival_detail(slug):
    festival_date = request.args.get("date")
    
    if not festival_date:
        return "Invalid or missing date parameter", 400

    # Fetch the festival using the festival name (slug) and date dynamically
    festival = get_festival_by_slug(slug, festival_date)

    if festival is None:
        return f"Festival with name '{slug}' and date '{festival_date}' not found", 404

    # Render festival detail page with the festival data
    return render_template("festival_detail.html", festival=festival, festival_date=festival_date)

# Route to show the festivals UI page
@app.route("/festivals-ui")
def festivals_ui():
    return render_template("festivals.html")

# Panchang API Route
@app.route("/panchang")
def get_panchang():
    date_str = request.args.get("date")
    if not date_str:
        today = datetime.today().date()  # Use datetime.today() instead of datetime.now()
    else:
        try:
            today = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    result = calculate_panchang(today.year, today.month, today.day)
    return jsonify(result)

# Festivals Route
@app.route("/festivals", methods=["GET"])
def festival_route():
    date_str = request.args.get("date")  # Date should be passed in the URL like ?date=YYYY-MM-DD
    try:
        query_date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else datetime.today().date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    start = query_date.replace(day=1)  # Start of the month
    if query_date.month == 12:
        end = query_date.replace(year=query_date.year + 1, month=1, day=1)
    else:
        end = query_date.replace(month=query_date.month + 1, day=1)  # End of the month

    all_festivals = calculate_festivals(start, end)

    # Ensure the 'weekday' field is included in each festival data
    for festival in all_festivals:
        festival["weekday"] = festival.get("weekday", "Unknown")  # Add fallback for missing weekday

    return jsonify({
        "month": query_date.strftime("%B %Y"),
        "festivals": all_festivals
    })

# Ekadashi API Route
@app.route("/ekadashi")
def ekadashi_route():
    # Accept ?year=YYYY param from frontend
    year = request.args.get("year", default=None, type=int)

    if year is None:
        start = date.today()
        end = date(start.year, 12, 31)
    else:
        start = date(year, 1, 1)
        end = date(year, 12, 31)

    result = find_ekadashis(start, end)
    return jsonify(result)


@app.route("/ekadashi1")
def show_ekadashi_page():
    return render_template("ekadashi.html")

@app.route("/ekadashi/<slug>-date-time")
def ekadashi_detail(slug):
    year = request.args.get("year")
    if not year or not year.isdigit():
        return "Invalid or missing year parameter", 400

    year = int(year)
    
    # Correct usage of date
    all_ekadashis = find_ekadashis(date(year, 1, 1), date(year, 12, 31))

    ek = next((e for e in all_ekadashis if e['slug'] == slug), None)

    if not ek:
        return f"Ekadashi with slug '{slug}' not found for {year}", 404

    ek_date = date.fromisoformat(ek["iso_date"])
    panchang = calculate_panchang(ek_date.year, ek_date.month, ek_date.day)

    return render_template("ekadashi_detail.html", ekadashi=ek, panchang=panchang)

    # Calculate panchang details for the Ekadashi
    ekadashi_date = date.fromisoformat(ekadashi["iso_date"])
    panchang = calculate_panchang(ekadashi_date.year, ekadashi_date.month, ekadashi_date.day)

    # Render the detail page
    return render_template("ekadashi_detail.html", ekadashi=ekadashi, panchang=panchang)

# Function to generate slug from festival name (if not already done)
def generate_slug(festival_name):
    return festival_name.lower().replace(" ", "-").replace(",", "").replace(".", "")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
