# backend/panchang/festival_calculator.py

import datetime
import swisseph as swe
import pytz
from panchang.core import calculate_panchang  # assumes your astronomical panchang logic is in core.py

def get_ekadashis(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    EKADASHI_NAME_MAP = {
        "Chaitra-Shukla": "Kamada Ekadashi",
        "Chaitra-Krishna": "Papmochani Ekadashi",
        "Vaishakha-Shukla": "Mohini Ekadashi",
        "Vaishakha-Krishna": "Apara Ekadashi",
        "Jyeshtha-Shukla": "Nirjala Ekadashi",
        "Jyeshtha-Krishna": "Yogini Ekadashi",
        "Ashadha-Shukla": "Devshayani Ekadashi",
        "Ashadha-Krishna": "Kamika Ekadashi",
        "Shravana-Shukla": "Shravana Putrada Ekadashi",
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
        "Magha-Krishna": "Katyayani Ekadashi",
        "Phalguna-Shukla": "Amalaki Ekadashi",
        "Phalguna-Krishna": "Vijaya Ekadashi"
    }

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt = india_tz.localize(dt)

        p = calculate_panchang(dt.year, dt.month, dt.day)
        
        # Log the panchang data to see if the 'weekday' key exists
        print("Panchang Data:", p)  # Log the full data to check its contents

        # Safely access 'weekday', defaulting to 'Unknown' if it's missing
        weekday = p.get("weekday", "Unknown")

        if p["tithi"]["name"] == "Ekadashi":
            key = f'{p["month"]["purnimanta"]}-{p["paksha"]}'
            name = EKADASHI_NAME_MAP.get(key, "Ekadashi")

            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": name,
                "tithi": p["tithi"]["name"],
                "paksha": p["paksha"],
                "month": p["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += datetime.timedelta(days=1)

    return results




def match_festival(tithi, paksha, month):
    if tithi == "Purnima" and paksha == "Shukla" and month == "Ashadha":
        return "Guru Purnima"
    if tithi == "Chaturdashi" and paksha == "Krishna" and month == "Phalguna":
        return "Maha Shivratri"
    if tithi == "Purnima" and paksha == "Shukla" and month == "Phalguna":
        return "Holi"
    if tithi == "Navami" and paksha == "Shukla" and month == "Chaitra":
        return "Ram Navami"
    if tithi == "Purnima" and paksha == "Shukla" and month == "Chaitra":
        return "Hanuman Jayanti"
    if tithi == "Tritiya" and paksha == "Shukla" and month == "Vaishakha":
        return "Akshaya Tritiya"
    if tithi == "Dwitiya" and paksha == "Shukla" and month == "Ashadha":
        return "Rath Yatra"
    if tithi == "Ashtami" and paksha == "Krishna" and month == "Bhadrapada":
        return "Krishna Janmashtami"
    if tithi == "Chaturthi" and paksha == "Shukla" and month == "Bhadrapada":
        return "Ganesh Chaturthi"
    if tithi == "Pratipada" and paksha == "Shukla" and month == "Ashwin":
        return "Navratri Begins"
    if tithi == "Ashtami" and paksha == "Shukla" and month == "Ashwin":
        return "Durga Ashtami"
    if tithi == "Dashami" and paksha == "Shukla" and month == "Ashwin":
        return "Dussehra"
    if tithi == "Purnima" and paksha == "Shukla" and month == "Ashwin":
        return "Sharad Purnima"
    if tithi == "Chaturthi" and paksha == "Krishna" and month == "Kartika":
        return "Karwa Chauth"
    if tithi == "Trayodashi" and paksha == "Krishna" and month == "Kartika":
        return "Dhanteras"
    if tithi == "Chaturdashi" and paksha == "Krishna" and month == "Kartika":
        return "Naraka Chaturdashi"
    if tithi == "Amavasya" and paksha == "Krishna" and month == "Kartika":
        return "Diwali"
    if tithi == "Pratipada" and paksha == "Shukla" and month == "Kartika":
        return "Govardhan Puja"
    if tithi == "Dwitiya" and paksha == "Shukla" and month == "Kartika":
        return "Bhai Dooj"
    if tithi == "Purnima" and paksha == "Shukla" and month == "Kartika":
        return "Dev Diwali"
    return None




def get_sankashti_chaturthi(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Log data to understand its structure
        print(data)  # Log the full data to check its contents

        # Safely access the 'weekday' key, defaulting to "Unknown" if it's missing
        weekday = data.get("weekday", "Unknown")

        if (
            data["tithi"]["name"].lower() == "chaturthi"
            and data["paksha"].lower() == "krishna"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Sankashti Chaturthi",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += datetime.timedelta(days=1)

    return results





def calculate_festival_days(start_date, end_date):
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        # Adjust for 6:00 AM IST to match Indian festival day logic
        current_dt = datetime.datetime.combine(current, datetime.time(6, 0))
        localized_dt = india_tz.localize(current_dt)
        dt_ist = localized_dt

        adjusted_date = dt_ist.date()
        data = calculate_panchang(adjusted_date.year, adjusted_date.month, adjusted_date.day)

        tithi = data["tithi"]["name"]
        paksha = data["paksha"]
        month = data["month"]["purnimanta"]

        festival_name = match_festival(tithi, paksha, month)

       
        if festival_name:
            results.append({
                "date": adjusted_date.isoformat(),
                "readable_date": dt_ist.strftime("%B %d, %Y"),
                "name": festival_name,
                "tithi": tithi,
                "paksha": paksha,
                "month": month,
                "weekday": dt_ist.strftime("%A")
            })

        current += datetime.timedelta(days=1)

    return results




def get_kalashtami(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Log the data to see its contents
        print(data)  # Log the full data to check its contents

        # Safely access the 'weekday' key, defaulting to "Unknown" if it's missing
        weekday = data.get("weekday", "Unknown")

        if (
            data["tithi"]["name"].lower() == "ashtami"
            and data["paksha"].lower() == "krishna"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Kalashtami",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += datetime.timedelta(days=1)

    return results




def get_masik_krishna_janmashtami(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Log data to see what it contains (for debugging)
        print("Panchang Data:", data)

        # Safely access 'weekday' using .get() and fallback to "Unknown" if not available
        weekday = data.get("weekday", "Unknown")  # Default to "Unknown" if weekday is missing

        if (
            data["tithi"]["name"] == "Chaturdashi"
            and data["paksha"].lower() == "krishna"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Masik Krishna Janmashtami",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += datetime.timedelta(days=1)

    return results


def get_rohini_vrat(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        if data.get("nakshatra", {}).get("name", "").lower() == "rohini":
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Rohini Vrat",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "nakshatra": data["nakshatra"]["name"],
                "weekday": data["weekday"]
            })

        current += datetime.timedelta(days=1)

    return results


def get_masik_karthigai(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        if data.get("nakshatra", {}).get("name", "").lower() == "krittika":
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Masik Karthigai",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "nakshatra": data["nakshatra"]["name"],
                "weekday": data["weekday"]
            })

        current += datetime.timedelta(days=1)

    return results



def get_darsha_anvadhan_ishti(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    india_tz = pytz.timezone("Asia/Kolkata")

    prev_day_panchang = None

    current = start_date
    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)
        p = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Log the panchang data to see if the 'weekday' field exists
        print("Panchang Data:", p)  # Log the full p object

        # Safely access 'weekday', defaulting to 'Unknown' if it is missing
        weekday = p.get("weekday", "Unknown")

        # Darsha Amavasya
        if p["tithi"]["name"] == "Amavasya":
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Darsha Amavasya",
                "tithi": p["tithi"]["name"],
                "paksha": p["paksha"],
                "month": p["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        # Anvadhan
        if p["tithi"]["name"] in ["Amavasya", "Purnima"]:
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Anvadhan",
                "tithi": p["tithi"]["name"],
                "paksha": p["paksha"],
                "month": p["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        # Ishti (Day After Amavasya or Purnima)
        if prev_day_panchang and prev_day_panchang["tithi"]["name"] in ["Amavasya", "Purnima"]:
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Ishti",
                "tithi": p["tithi"]["name"],
                "paksha": p["paksha"],
                "month": p["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        prev_day_panchang = p
        current += datetime.timedelta(days=1)

    return results




def get_monthly_purnima_amavasya(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        current_dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(current_dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Safely get the 'weekday' value, defaulting to "Unknown" if missing
        weekday = data.get("weekday", "Unknown")

        tithi = data["tithi"]["name"].lower()
        paksha = data["paksha"].lower()

        if tithi == "purnima" and paksha == "shukla":
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Purnima",
                "tithi": "Purnima",
                "paksha": "Shukla",
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Use the safely retrieved 'weekday'
            })

        elif tithi == "amavasya" and paksha == "krishna":
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Amavasya",
                "tithi": "Amavasya",
                "paksha": "Krishna",
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Use the safely retrieved 'weekday'
            })

        current += datetime.timedelta(days=1)

    return results




def get_pradosh_vrat(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        # Combine current date with time to get 6 AM IST
        sunset_time = datetime.datetime.combine(current, datetime.time(18, 30))
        dt_ist = india_tz.localize(sunset_time)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Log data to understand its structure
        print(data)  # Log the full data to check its contents

        # Safely access the 'weekday' key, defaulting to "Unknown" if it's missing
        weekday = data.get("weekday", "Unknown")

        if data["tithi"]["name"].lower() == "trayodashi":
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Pradosh Vrat",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += datetime.timedelta(days=1)

    return results





def get_navratri_periods(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        ist = india_tz.localize(dt)
        data = calculate_panchang(ist.year, ist.month, ist.day)

        # Use .get() to safely access 'weekday'
        weekday = data.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        if (
            data["tithi"]["name"].lower() == "pratipada"
            and data["paksha"].lower() == "shukla"
            and data["month"]["purnimanta"].lower() in ["chaitra", "ashwin"]
        ):
            navratri_type = "Chaitra Navratri" if data["month"]["purnimanta"].lower() == "chaitra" else "Shardiya Navratri"

            for i in range(9):
                day = current + datetime.timedelta(days=i)
                ddt = datetime.datetime.combine(day, datetime.time(6, 0))
                d_ist = india_tz.localize(ddt)
                p = calculate_panchang(d_ist.year, d_ist.month, d_ist.day)

                results.append({
                    "date": day.isoformat(),
                    "readable_date": day.strftime("%B %d, %Y"),
                    "name": f"{navratri_type} Day {i+1}",
                    "tithi": p["tithi"]["name"],
                    "paksha": p["paksha"],
                    "month": p["month"]["purnimanta"],
                    "weekday": p.get("weekday", "Unknown")  # Safely get weekday
                })

            # Skip ahead 9 days
            current += datetime.timedelta(days=9)
            continue

        current += datetime.timedelta(days=1)

    return results



def get_masik_durgashtami(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        current_dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(current_dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Safe access for 'weekday' using .get() to avoid KeyError
        weekday = data.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        if (
            data["tithi"]["name"].lower() == "ashtami"
            and data["paksha"].lower() == "shukla"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Masik Durgashtami",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Use the safely retrieved 'weekday'
            })

        current += datetime.timedelta(days=1)

    return results



def get_masik_shivratri(start_date, end_date):
    from panchang.core import calculate_panchang
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        dt = datetime.datetime.combine(current, datetime.time(6, 0))
        dt_ist = india_tz.localize(dt)

        data = calculate_panchang(dt_ist.year, dt_ist.month, dt_ist.day)

        # Using .get() to safely access 'weekday' key
        weekday = data.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        if (
            data["tithi"]["name"] == "Chaturdashi"
            and data["paksha"].lower() == "krishna"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Masik Shivratri",
                "tithi": data["tithi"]["name"],
                "paksha": data["paksha"],
                "month": data["month"]["purnimanta"],
                "weekday": weekday  # Use the safe value of 'weekday'
            })

        current += datetime.timedelta(days=1)

    return results




def get_sankrantis(start_date, end_date):
    results = []
    india_tz = pytz.timezone("Asia/Kolkata")
    prev_long = None
    prev_sign = None

    current = start_date
    while current <= end_date:
        jd = swe.julday(current.year, current.month, current.day, 5.5)
        sun_long = swe.calc_ut(jd, swe.SUN)[0][0]
        sun_sign_index = int(sun_long / 30)
        sun_sign = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ][sun_sign_index]

        if prev_sign and sun_sign != prev_sign:
            # This is Sankranti day (Sun changed sign)
            dt = datetime.datetime.combine(current, datetime.time(6, 0))
            dt_ist = india_tz.localize(dt)
            if sun_sign == "Aquarius":
                results.append({
                    "date": current.isoformat(),
                    "readable_date": dt_ist.strftime("%B %d, %Y"),
                    "name": "Kumbha Sankranti",
                    "sign": sun_sign,
                    "weekday": dt_ist.strftime("%A")
                })

        prev_sign = sun_sign
        current += datetime.timedelta(days=1)

    return results



def get_vasant_panchami(start, end):
    from datetime import timedelta
    from .core import calculate_panchang
    results = []

    current = start
    while current < end:
        p = calculate_panchang(current.year, current.month, current.day)

        # Log the panchang data to inspect its structure (optional for debugging)
        print("Panchang Data:", p)

        # Safely access 'weekday', defaulting to 'Unknown' if it's not present
        weekday = p.get("weekday", "Unknown")  # Default to "Unknown" if weekday is missing

        if (
            p["tithi"]["name"] == "Panchami"
            and p["paksha"] == "Shukla"
            and p["month"]["purnimanta"] == "Magha"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Vasant Panchami",
                "tithi": p["tithi"]["name"],
                "paksha": p["paksha"],
                "month": p["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })
        current += timedelta(days=1)
    return results





from datetime import timedelta
from .core import calculate_panchang

def get_ratha_saptami(start, end):
    results = []
    current = start
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Safely access 'weekday', defaulting to 'Unknown' if missing
        weekday = panchang.get("weekday", "Unknown")  # Use .get() to prevent KeyError

        # Log the panchang data to check its structure (for debugging)
        print("Panchang Data:", panchang)

        if (
            panchang["tithi"]["name"] == "Saptami"
            and panchang["paksha"] == "Shukla"
            and panchang["month"]["purnimanta"] == "Magha"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Ratha Saptami",
                "tithi": panchang["tithi"]["name"],
                "paksha": panchang["paksha"],
                "month": panchang["month"]["purnimanta"],
                "weekday": weekday  # Safely assign 'weekday' here
            })

        current += timedelta(days=1)

    return results

def get_bhishma_ashtami(start, end):
    results = []
    current = start

    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Safely access the 'weekday' key using .get() to prevent KeyError
        weekday = panchang.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        # Log the data to inspect its structure (for debugging purposes)
        print("Panchang Data:", panchang)  # Check panchang data if 'weekday' exists

        if (
            panchang["tithi"]["name"] == "Ashtami"
            and panchang["paksha"] == "Shukla"
            and panchang["month"]["purnimanta"] == "Magha"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Bhishma Ashtami",
                "tithi": panchang["tithi"]["name"],
                "paksha": panchang["paksha"],
                "month": panchang["month"]["purnimanta"],
                "weekday": weekday  # Use the safely retrieved 'weekday'
            })

        current += timedelta(days=1)

    return results

def get_nag_panchami(start, end):
    results = []
    current = start
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Log the full panchang data to understand its structure
        print("Panchang Data:", panchang)  # Log the full data to check if 'weekday' exists

        # Use .get() to safely access the 'weekday' key, providing a default value if missing
        weekday = panchang.get("weekday", "Unknown")

        if (
            panchang["tithi"]["name"] == "Panchami" and
            panchang["paksha"] == "Shukla" and
            panchang["month"]["purnimanta"] == "Shravana"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Nag Panchami",
                "tithi": panchang["tithi"]["name"],
                "paksha": panchang["paksha"],
                "month": panchang["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += timedelta(days=1)

    return results


def get_raksha_bandhan(start, end):
    results = []
    current = start
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Log the panchang data to inspect its structure
        print("Panchang Data:", panchang)  # Log data to see if 'weekday' is missing

        # Use .get() to safely access 'weekday' to avoid KeyError
        weekday = panchang.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        if (
            panchang["tithi"]["name"] == "Purnima" and
            panchang["paksha"] == "Shukla" and
            panchang["month"]["purnimanta"] == "Shravana"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Raksha Bandhan",
                "tithi": panchang["tithi"]["name"],
                "paksha": panchang["paksha"],
                "month": panchang["month"]["purnimanta"],
                "weekday": weekday  # Use the safely retrieved 'weekday'
            })

        current += timedelta(days=1)

    return results

def get_pitru_paksha_start(start, end):
    results = []
    current = start
    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)
        if panchang["tithi"]["name"] == "Purnima" and panchang["paksha"] == "Shukla" and panchang["month"]["purnimanta"] == "Bhadrapada":
            next_day = current + timedelta(days=1)
            p2 = calculate_panchang(next_day.year, next_day.month, next_day.day)

            # Safely check for the 'weekday' key in p2 before accessing it
            weekday = p2.get("weekday", "Unknown")  # Default to "Unknown" if missing

            results.append({
                "date": next_day.isoformat(),
                "readable_date": next_day.strftime("%B %d, %Y"),
                "name": "Pitru Paksha Begins",
                "tithi": p2["tithi"]["name"],
                "paksha": p2["paksha"],
                "month": p2["month"]["purnimanta"],
                "weekday": weekday  # Use the safely retrieved 'weekday'
            })
        current += timedelta(days=1)
    return results





def get_varalakshmi_vratam(start_date, end_date):
    from datetime import timedelta
    from .core import calculate_panchang
    results = []

    current = start_date
    while current <= end_date:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Log the panchang data to inspect its structure
        print("Panchang Data:", panchang)  # Log data to see if 'weekday' is missing

        # Use .get() to safely access 'weekday' to avoid KeyError
        weekday = panchang.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        if (
            panchang["paksha"] == "Shukla" and
            weekday == "Friday" and
            panchang["month"]["purnimanta"] == "Shravana"
        ):
            # Now check if Purnima occurs in the next 7 days (before Friday next week)
            lookahead = current
            purnima_found = False
            for _ in range(1, 8):
                lookahead += timedelta(days=1)
                p = calculate_panchang(lookahead.year, lookahead.month, lookahead.day)
                if p["tithi"]["name"] == "Purnima":
                    purnima_found = True
                    break

            if purnima_found:
                results.append({
                    "date": current.isoformat(),
                    "readable_date": current.strftime("%B %d, %Y"),
                    "name": "Varalakshmi Vratam",
                    "tithi": panchang["tithi"]["name"],
                    "paksha": panchang["paksha"],
                    "month": panchang["month"]["purnimanta"],
                    "weekday": weekday  # Use the safely retrieved 'weekday'
                })

        current += timedelta(days=1)

    return results





def get_ganga_dussehra(start_date, end_date):
    results = []
    current = start_date
    india_tz = pytz.timezone("Asia/Kolkata")

    while current <= end_date:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Log data to see the structure of the panchang data
        print("Panchang Data:", panchang)  # Log the full data to see if 'weekday' exists

        # Safely access the 'weekday' key, defaulting to "Unknown" if it's missing
        weekday = panchang.get("weekday", "Unknown")

        if (
            panchang["tithi"]["name"] == "Dashami" and
            panchang["paksha"] == "Shukla" and
            panchang["month"]["purnimanta"] == "Jyeshtha"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Ganga Dussehra",
                "tithi": panchang["tithi"]["name"],
                "paksha": panchang["paksha"],
                "month": panchang["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += timedelta(days=1)

    return results







def get_vaibhav_lakshmi_vrat(start_date, end_date):
    from datetime import timedelta
    from .core import calculate_panchang
    results = []

    current = start_date
    while current <= end_date:
        panchang = calculate_panchang(current.year, current.month, current.day)

        # Log the panchang data to inspect its contents
        print("Panchang Data:", panchang)  # Log the full data to see if 'weekday' is present

        # Safely access the 'weekday' key, defaulting to "Unknown" if it's missing
        weekday = panchang.get("weekday", "Unknown")  # Default to "Unknown" if 'weekday' is missing

        if (
            panchang["paksha"] == "Shukla" and
            weekday == "Friday" and
            panchang["month"]["purnimanta"] == "Shravana"
        ):
            results.append({
                "date": current.isoformat(),
                "readable_date": current.strftime("%B %d, %Y"),
                "name": "Varalakshmi Vratam",
                "tithi": panchang["tithi"]["name"],
                "paksha": panchang["paksha"],
                "month": panchang["month"]["purnimanta"],
                "weekday": weekday  # Safely assign weekday here
            })

        current += timedelta(days=1)

    return results






def get_holi(start, end):
    results = []
    current = start
    while current <= end:
        ppanchang = calculate_panchang(current.year, current.month, current.day)
        if (
            panchang["tithi"] == "Purnima"
            and panchang["paksha"] == "Shukla"
            and panchang["month"] == "Phalguna"
        ):
            results.append({
                "name": "Holi (Holika Dahan)",
                "date": current.strftime("%Y-%m-%d"),
                "readable_date": current.strftime("%d %B %Y"),
                "weekday": current.strftime("%A"),
                "tithi": panchang["tithi"],
                "paksha": panchang["paksha"],
                "month": panchang["month"],
            })
        current += timedelta(days=1)
    return results

def get_hanuman_jayanti(start, end):
    results = []
    current = start
    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)
        if (
            panchang["tithi"] == "Purnima"
            and panchang["paksha"] == "Shukla"
            and panchang["month"] == "Chaitra"
        ):
            results.append({
                "name": "Hanuman Jayanti",
                "date": current.strftime("%Y-%m-%d"),
                "readable_date": current.strftime("%d %B %Y"),
                "weekday": current.strftime("%A"),
                "tithi": panchang["tithi"],
                "paksha": panchang["paksha"],
                "month": panchang["month"],
            })
        current += timedelta(days=1)
    return results

def get_akshaya_tritiya(start, end):
    results = []
    current = start
    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)
        if (
            panchang["tithi"] == "Tritiya"
            and panchang["paksha"] == "Shukla"
            and panchang["month"] == "Vaishakha"
        ):
            results.append({
                "name": "Akshaya Tritiya",
                "date": current.strftime("%Y-%m-%d"),
                "readable_date": current.strftime("%d %B %Y"),
                "weekday": current.strftime("%A"),
                "tithi": panchang["tithi"],
                "paksha": panchang["paksha"],
                "month": panchang["month"],
            })
        current += timedelta(days=1)
    return results

def get_ratha_yatra(start, end):
    results = []
    current = start
    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)
        if (
            panchang["tithi"] == "Dwitiya"
            and panchang["paksha"] == "Shukla"
            and panchang["month"] == "Ashadha"
        ):
            results.append({
                "name": "Ratha Yatra",
                "date": current.strftime("%Y-%m-%d"),
                "readable_date": current.strftime("%d %B %Y"),
                "weekday": current.strftime("%A"),
                "tithi": panchang["tithi"],
                "paksha": panchang["paksha"],
                "month": panchang["month"],
            })
        current += timedelta(days=1)
    return results

def get_sharad_purnima(start, end):
    results = []
    current = start
    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)
        if (
            panchang["tithi"] == "Purnima"
            and panchang["paksha"] == "Shukla"
            and panchang["month"] == "Ashwin"
        ):
            results.append({
                "name": "Sharad Purnima",
                "date": current.strftime("%Y-%m-%d"),
                "readable_date": current.strftime("%d %B %Y"),
                "weekday": current.strftime("%A"),
                "tithi": panchang["tithi"],
                "paksha": panchang["paksha"],
                "month": panchang["month"],
            })
        current += timedelta(days=1)
    return results

def get_diwali_lakshmi_puja(start, end):
    results = []
    current = start
    while current <= end:
        panchang = calculate_panchang(current.year, current.month, current.day)
        if (
            panchang["tithi"] == "Amavasya"
            and panchang["paksha"] == "Krishna"
            and panchang["month"] == "Kartika"
        ):
            results.append({
                "name": "Diwali (Lakshmi Puja)",
                "date": current.strftime("%Y-%m-%d"),
                "readable_date": current.strftime("%d %B %Y"),
                "weekday": current.strftime("%A"),
                "tithi": panchang["tithi"],
                "paksha": panchang["paksha"],
                "month": panchang["month"],
            })
        current += timedelta(days=1)
    return results
