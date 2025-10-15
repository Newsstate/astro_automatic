from flask import Flask, request, jsonify, render_template, abort
from flask_cors import CORS
from panchang.calculator import calculate_panchang
from panchang.ekadashi import find_ekadashis
from panchang.festivals import calculate_festivals
from panchang.festival_calculator import calculate_festival_days
from datetime import datetime, date

# --- CORS Configuration ---
# Including all potential frontend domains (www/non-www and the domain from the original error)
allowed_origins = [
    "https://www.asthaguru.com",
    "https://asthaguru.com",
    "https://www.khabar24live.com",
    "https://khabar24live.com",
    # If the widget is being tested locally, you might also add:
    # "http://localhost:port_number"
]

# Initialize the Flask app and enable CORS
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app, 
     origins=allowed_origins,
     supports_credentials=True # Needed if you ever use cookies/sessions
)

# --- Helper Functions ---
def generate_slug(festival_name):
    """Generates a URL-friendly slug from a festival name."""
    return festival_name.lower().replace(" ", "-").replace(",", "").replace(".", "")

def get_festival_by_slug(slug, festival_date):
    """
    Finds a festival by its slug and date.
    Note: This is an expensive operation as it calculates all festivals.
    Consider caching or a database for production.
    """
    # Adjust date range as needed for the lookup
    # Using a simplified 2024 range for demonstration
    all_festivals = calculate_festival_days(date(2024, 1, 1), date(2024, 12, 31))
    
    # Match festival by both slug (festival name) and date
    festival = next((f for f in all_festivals if generate_slug(f['name']) == slug and f['date'] == festival_date), None)
    return festival

# --- Routes ---
@app.route("/")
def show_panchang_page():
    """Root route to serve the index.html page."""
    return render_template("index.html")

@app.route("/<slug>-date-time")
def festival_detail(slug):
    """Route to show details for a specific festival based on slug and date."""
    festival_date = request.args.get("date")
    
    if not festival_date:
        return abort(400, description="Missing date parameter")

    try:
        parsed_date = datetime.strptime(festival_date, "%Y-%m-%d").date()
    except ValueError:
        return abort(400, description="Invalid date format. Use YYYY-MM-DD")

    festival = get_festival_by_slug(slug, parsed_date)

    if festival is None:
        return abort(404, description=f"Festival '{slug}' on {festival_date} not found")

    return render_template(
        "festival_detail.html",
        festival=festival,
        festival_date=parsed_date
    )

@app.route("/festivals-ui")
def festivals_ui():
    """Route to show the festivals UI page."""
    return render_template("festivals.html")

@app.route("/panchang")
def get_panchang():
    """API route to get panchang data for a given date."""
    date_str = request.args.get("date")
    if not date_str:
        today = datetime.today().date()
    else:
        try:
            today = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Ensure the panchang calculation function is available in your environment
    try:
        result = calculate_panchang(today.year, today.month, today.day)
    except Exception as e:
        # In a real app, you'd log the full error, but for the user:
        return jsonify({"error": f"Panchang calculation failed on the server: {str(e)}"}), 500

    return jsonify(result)

@app.route("/festivals", methods=["GET"])
def festival_route():
    """API route to get festival data for a given date range."""
    date_str = request.args.get("date")
    try:
        query_date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else datetime.today().date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    start = query_date.replace(day=1)
    if query_date.month == 12:
        end = query_date.replace(year=query_date.year + 1, month=1, day=1)
    else:
        end = query_date.replace(month=query_date.month + 1, day=1)

    all_festivals = calculate_festivals(start, end)
    
    # NOTE: The 'weekday' field should be added in calculate_festivals or core.py.
    # This loop is a temporary fix if the underlying functions are not updated.
    for festival in all_festivals:
        if "weekday" not in festival:
             # Calculate weekday if missing
             festival_date = datetime.strptime(festival["date"], "%Y-%m-%d").date()
             festival["weekday"] = festival_date.strftime("%A")

    return jsonify({
        "month": query_date.strftime("%B %Y"),
        "festivals": all_festivals
    })

@app.route("/ekadashi")
def ekadashi_route():
    """API route to get ekadashi dates for a given year or today's year."""
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
    """Route to show the ekadashi UI page."""
    return render_template("ekadashi.html")

@app.route("/ekadashi/<slug>-date-time")
def ekadashi_detail(slug):
    """Route to show details for a specific ekadashi."""
    year = request.args.get("year")
    if not year or not year.isdigit():
        return "Invalid or missing year parameter", 400

    year = int(year)
    
    all_ekadashis = find_ekadashis(date(year, 1, 1), date(year, 12, 31))
    ek = next((e for e in all_ekadashis if e.get('slug') == slug), None)

    if not ek:
        return f"Ekadashi with slug '{slug}' not found for {year}", 404

    ek_date = date.fromisoformat(ek["iso_date"])
    panchang = calculate_panchang(ek_date.year, ek_date.month, ek_date.day)

    return render_template("ekadashi_detail.html", ekadashi=ek, panchang=panchang)


if __name__ == '__main__':
    app.run(debug=True)
