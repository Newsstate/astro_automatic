import swisseph as swe
import datetime
import pytz

TITHI_SIZE = 12.0

LUNAR_MONTHS = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha",
    "Shravana", "Bhadrapada", "Ashwin", "Kartika",
    "Margashirsha", "Pausha", "Magha", "Phalguna"
]

def get_tithi_name(index):
    names = [
        "Pratipada", "Dvitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi",
        "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi",
        "Trayodashi", "Chaturdashi", "Purnima", "Amavasya"
    ]
    return names[index % 15]

def get_purnimanta_month(sun_long):
    solar_index = int((sun_long + 15) % 360 / 30)
    return LUNAR_MONTHS[solar_index]

def calculate_panchang(year, month, day, hour=6, minute=0, latitude=28.6139, longitude=77.2090):
    swe.set_topo(longitude, latitude, 0)
    jd = swe.julday(year, month, day, hour + minute / 60.0)
    sun_long = swe.calc_ut(jd, swe.SUN)[0][0]
    moon_long = swe.calc_ut(jd, swe.MOON)[0][0]
    
    tithi_num = int(((moon_long - sun_long) % 360) / TITHI_SIZE)
    paksha = "Shukla" if tithi_num < 15 else "Krishna"
    month_name = get_purnimanta_month(sun_long)

    return {
        "tithi": {
            "name": get_tithi_name(tithi_num),
            "number": tithi_num
        },
        "paksha": paksha,
        "month": {
            "purnimanta": month_name
        }
    }

def get_tithi_at_sunrise(year, month, day):
    return calculate_panchang(year, month, day, hour=6, minute=0)
