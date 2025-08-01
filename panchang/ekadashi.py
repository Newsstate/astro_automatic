from datetime import datetime, timedelta, time
import pytz

from panchang.core import get_tithi_at_sunrise


EKADASHI_NAME_MAP = {
    "Chaitra-Shukla": "Kamada Ekadashi",
    "Chaitra-Krishna": "Papmochani Ekadashi",
    "Vaishakha-Shukla": "Mohini Ekadashi",
    "Vaishakha-Krishna": "Apara Ekadashi",
    "Jyeshtha-Shukla": "Nirjala Ekadashi",
    "Jyeshtha-Krishna": "Yogini Ekadashi",
    "Ashadha-Shukla": "Devshayani Ekadashi",
    "Ashadha-Krishna": "Kamika Ekadashi",
    "Shravana-Shukla": "Putrada Ekadashi",
    "Shravana-Krishna": "Aja Ekadashi",
    "Bhadrapada-Shukla": "Parivartini Ekadashi",
    "Bhadrapada-Krishna": "Indira Ekadashi",
    "Ashwin-Shukla": "Papankusha Ekadashi",
    "Ashwin-Krishna": "Rama Ekadashi",
    "Kartika-Shukla": "Prabodhini Ekadashi",
    "Kartika-Krishna": "Rama Ekadashi",
    "Margashirsha-Shukla": "Mokshada Ekadashi",
    "Margashirsha-Krishna": "Utpanna Ekadashi",
    "Pausha-Shukla": "Pausha Putrada Ekadashi",
    "Pausha-Krishna": "Saphala Ekadashi",
    "Magha-Shukla": "Shattila Ekadashi",
    "Magha-Krishna": "Jaya Ekadashi",
    "Phalguna-Shukla": "Amalaki Ekadashi",
    "Phalguna-Krishna": "Vijaya Ekadashi"
}

def get_ekadashi_name(month, paksha):
    return EKADASHI_NAME_MAP.get(f"{month}-{paksha}", "Ekadashi")

def get_parana_details(ekadashi_date):
    next_day = ekadashi_date + timedelta(days=1)
    details = get_tithi_at_sunrise(next_day.year, next_day.month, next_day.day)
    return {
        "parana_date": next_day.isoformat(),
        "sunrise": "06:00 AM",
        "dwadashi_tithi": details["tithi"],
        "paksha": details["paksha"]
    }

def find_ekadashis(start_date, end_date):
    ekadashis = []
    current_date = start_date

    while current_date <= end_date:
        sunrise_dt = datetime.combine(current_date, time(6, 0))
        tithi_info = get_tithi_at_sunrise(sunrise_dt.year, sunrise_dt.month, sunrise_dt.day)

        if tithi_info["tithi"]["name"] == "Ekadashi":
            month = tithi_info["month"]["purnimanta"]
            paksha = tithi_info["paksha"]
            name = get_ekadashi_name(month, paksha)
            slug = name.lower().replace(" ", "-").replace("’", "").replace("'", "")
            parana = get_parana_details(current_date)

            ekadashis.append({
                "readable_date": current_date.strftime("%B %d, %Y, %A"),
                "iso_date": current_date.isoformat(),
                "name": name,
                "slug": slug,
                "weekday": current_date.strftime("%A"),
                "tithi": "Ekadashi",
                "nakshatra": tithi_info.get("nakshatra", ""),
                "paksha": paksha,
                "month": month,
                "parana": parana
            })

        current_date += timedelta(days=1)

    return ekadashis