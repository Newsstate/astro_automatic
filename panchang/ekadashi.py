import re
from datetime import timedelta, date, datetime
from panchang.calculator import calculate_panchang

# Ekadashi Name Lookup (Purnimanta system)
EKADASHI_NAME_MAP = {
    "Chaitra-Shukla": "कामदा एकादशी",
"Chaitra-Krishna": "पापमोचनी एकादशी",
"Vaishakha-Shukla": "मोहिनी एकादशी",
"Vaishakha-Krishna": "अपरा एकादशी",
"Jyeshtha-Shukla": "निर्जला एकादशी",
"Jyeshtha-Krishna": "योगिनी एकादशी",
"Ashadha-Shukla": "देवशयनी एकादशी",
"Ashadha-Krishna": "कामिका एकादशी",
"Shravana-Shukla": "पुत्रदा एकादशी",
"Shravana-Krishna": "अजा एकादशी",
"Bhadrapada-Shukla": "परिवर्तिनी एकादशी",
"Bhadrapada-Krishna": "इन्दिरा एकादशी",
"Ashwin-Shukla": "पापांकुशा एकादशी",
"Ashwin-Krishna": "पसांकुशा एकादशी",
"Kartika-Shukla": "प्रबोधिनी एकादशी",
"Kartika-Krishna": "रमा एकादशी",
"Margashirsha-Shukla": "मोक्षदा एकादशी",
"Margashirsha-Krishna": "उत्पन्ना एकादशी",
"Pausha-Shukla": "पुत्रदा एकादशी",
"Pausha-Krishna": "सफल एकादशी",
"Magha-Shukla": "षट्तिला एकादशी",
"Magha-Krishna": "कात्यायनी एकादशी",
"Phalguna-Shukla": "आमलकी एकादशी",
"Phalguna-Krishna": "विजया एकादशी",
"Adhika-Shukla": "पद्मिनी एकादशी",
"Adhika-Krishna": "परमा एकादशी"

}

def get_ekadashi_name(lunar_month, paksha):
    key = f"{lunar_month}-{paksha}"
    return EKADASHI_NAME_MAP.get(key, "Ekadashi")

def get_parana_time(ekadashi_date):
    next_day = ekadashi_date + timedelta(days=1)
    panchang = calculate_panchang(next_day.year, next_day.month, next_day.day)
    return {
        "parana_date": next_day.isoformat(),
        "sunrise": panchang["sunrise"],
        "tithi": panchang["tithi"]["name"],
        "paksha": panchang["paksha"]
    }

def generate_slug(name):
    return re.sub(r'[^\w\s-]', '', name).lower().replace(" ", "-")

def calculate_ekadashi_span_mock(ekadashi_date):
    start_dt = datetime.combine(ekadashi_date, datetime.min.time()).replace(hour=21, minute=26) - timedelta(days=1)
    end_dt = datetime.combine(ekadashi_date, datetime.min.time()).replace(hour=20, minute=15)
    return start_dt, end_dt

def format_datetime_range(start_dt, end_dt):
    return f"Begins - {start_dt.strftime('%I:%M %p, %b %d')}\nEnds - {end_dt.strftime('%I:%M %p, %b %d')}"

def find_ekadashis(start_date, end_date):
    ekadashis = []
    current = start_date
    while current <= end_date:
        p = calculate_panchang(current.year, current.month, current.day)
        if p["tithi"]["name"] == "Ekadashi":
            name = get_ekadashi_name(p["month"]["purnimanta"], p["paksha"])
            start_dt, end_dt = calculate_ekadashi_span_mock(current)
            ek = {
                "name": name,
                "slug": generate_slug(name),
                "iso_date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "tithi": "Ekadashi",
                "weekday": p["weekday"],
                "nakshatra": p["nakshatra"]["name"],
                "paksha": p["paksha"],
                "month": p["month"]["purnimanta"],
                "parana": get_parana_time(current),
                "start_time": format_datetime_range(start_dt, end_dt),
            }
            ekadashis.append(ek)
        current += timedelta(days=1)
    return ekadashis

