from datetime import datetime, timedelta
from panchang.calculator import calculate_panchang

def make_festival(date_obj, name):
    panchang = calculate_panchang(date_obj.year, date_obj.month, date_obj.day)
    return {
        "date": date_obj.isoformat(),
        "readable_date": date_obj.strftime("%B %d, %Y"),
        "name": name,
        "tithi": panchang["tithi"]["name"],
        "weekday": panchang["weekday"]
    }

def calculate_festivals(start_date, end_date):
    festivals = []
    current = start_date

    while current <= end_date:
        panchang = calculate_panchang(current.year, current.month, current.day)
        tithi = panchang["tithi"]["name"]
        paksha = panchang["paksha"]
        month = panchang["month"]["purnimanta"]

        # Rules for major Hindu festivals
        if tithi == "Purnima" and paksha == "Shukla" and month == "Ashadha":
            festivals.append(make_festival(current, "Guru Purnima"))
        elif tithi == "Chaturdashi" and paksha == "Krishna" and month == "Phalguna":
            festivals.append(make_festival(current, "Maha Shivratri"))
        elif tithi == "Purnima" and paksha == "Shukla" and month == "Phalguna":
            festivals.append(make_festival(current, "Holi"))
        elif tithi == "Navami" and paksha == "Shukla" and month == "Chaitra":
            festivals.append(make_festival(current, "Ram Navami"))
        elif tithi == "Purnima" and paksha == "Shukla" and month == "Chaitra":
            festivals.append(make_festival(current, "Hanuman Jayanti"))
        elif tithi == "Tritiya" and paksha == "Shukla" and month == "Vaishakha":
            festivals.append(make_festival(current, "Akshaya Tritiya"))
        elif tithi == "Ekadashi" and paksha == "Shukla" and month == "Jyeshtha":
            festivals.append(make_festival(current, "Nirjala Ekadashi"))
        elif tithi == "Dwitiya" and paksha == "Shukla" and month == "Ashadha":
            festivals.append(make_festival(current, "Jagannath Rath Yatra"))
        elif tithi == "Ashtami" and paksha == "Krishna" and month == "Bhadrapada":
            festivals.append(make_festival(current, "Krishna Janmashtami"))
        elif tithi == "Chaturthi" and paksha == "Shukla" and month == "Bhadrapada":
            festivals.append(make_festival(current, "Ganesh Chaturthi"))
        elif tithi == "Pratipada" and paksha == "Shukla" and month == "Ashwin":
            festivals.append(make_festival(current, "Navratri Begins"))
        elif tithi == "Ashtami" and paksha == "Shukla" and month == "Ashwin":
            festivals.append(make_festival(current, "Durga Ashtami"))
        elif tithi == "Dashami" and paksha == "Shukla" and month == "Ashwin":
            festivals.append(make_festival(current, "Dussehra"))
        elif tithi == "Purnima" and paksha == "Shukla" and month == "Ashwin":
            festivals.append(make_festival(current, "Sharad Purnima"))
        elif tithi == "Chaturthi" and paksha == "Krishna" and month == "Kartika":
            festivals.append(make_festival(current, "Karwa Chauth"))
        elif tithi == "Trayodashi" and paksha == "Krishna" and month == "Kartika":
            festivals.append(make_festival(current, "Dhanteras"))
        elif tithi == "Chaturdashi" and paksha == "Krishna" and month == "Kartika":
            festivals.append(make_festival(current, "Naraka Chaturdashi"))
        elif tithi == "Amavasya" and paksha == "Krishna" and month == "Kartika":
            festivals.append(make_festival(current, "Diwali"))
        elif tithi == "Pratipada" and paksha == "Shukla" and month == "Kartika":
            festivals.append(make_festival(current, "Govardhan Puja"))
        elif tithi == "Dwitiya" and paksha == "Shukla" and month == "Kartika":
            festivals.append(make_festival(current, "Bhai Dooj"))
        elif tithi == "Purnima" and paksha == "Shukla" and month == "Kartika":
            festivals.append(make_festival(current, "Dev Diwali"))

        current += timedelta(days=1)

    return festivals
