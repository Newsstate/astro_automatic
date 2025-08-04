import swisseph as swe
import datetime
import pytz
from panchang.rashi import get_rashi

NAKSHATRA_SIZE = 13.333333
TITHI_SIZE = 12.0
YOGA_SIZE = 13.333333

LUNAR_MONTHS = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha",
    "Shravana", "Bhadrapada", "Ashwin", "Kartika",
    "Margashirsha", "Pausha", "Magha", "Phalguna"
]

KARANA_NAMES = [
    "Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti",
    "Shakuni", "Chatushpada", "Naga", "Kimstughna"
]

def to_local_time(jd, tz='Asia/Kolkata'):
    utc_dt = datetime.datetime.utcfromtimestamp((jd - 2440587.5) * 86400.0)
    return utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(pytz.timezone(tz))

def get_purnimanta_month(sun_long):
    index = int((sun_long % 360) / 30)
    return LUNAR_MONTHS[(index + 0) % 12]

def get_amanta_month(sun_long):
    index = int((sun_long % 360) / 30)
    return LUNAR_MONTHS[index % 12]

def get_tithi_name(index):
    names = [
        "Pratipada", "Dvitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi",
        "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi",
        "Trayodashi", "Chaturdashi", "Purnima", "Amavasya"
    ]
    return names[index % 15]

def get_nakshatra_name(index):
    names = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashirsha",
        "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
        "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
        "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
        "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
        "Uttara Bhadrapada", "Revati"
    ]
    return names[index % 27]

def get_yoga_name(index):
    names = [
        "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda",
        "Sukarma", "Dhriti", "Shoola", "Ganda", "Vriddhi", "Dhruva",
        "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata", "Variyana",
        "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla",
        "Brahma", "Indra", "Vaidhriti"
    ]
    return names[index % 27]

def get_nakshatra_end(jd):
    moon_long = swe.calc_ut(jd, swe.MOON)[0][0]
    rem_deg = NAKSHATRA_SIZE - (moon_long % NAKSHATRA_SIZE)
    moon_speed = 13.2  # deg/day
    hours_to_end = rem_deg / moon_speed * 24
    end_time = to_local_time(jd + hours_to_end / 24)
    return end_time.strftime("%I:%M %p")

def get_karana_names(tithi_num):
    # First half of a tithi
    index1 = (tithi_num * 2) % 60
    index2 = (index1 + 1) % 60

    def karana_name(index):
        if index == 0:
            return KARANA_NAMES[10]  # Kimstughna
        elif index >= 57:
            return KARANA_NAMES[7 + (index - 57)]
        else:
            return KARANA_NAMES[index % 7]

    return karana_name(index1), karana_name(index2)

def get_sunrise_sunset(jd, lat, lon):
    try:
        rs = swe.rise_trans(jd, swe.SUN, lon, lat, rsmi=swe.CALC_RISE | swe.BIT_DISC_CENTER)
        sr = to_local_time(rs[1])
        ss = to_local_time(rs[2])
        return sr.strftime("%I:%M %p"), ss.strftime("%I:%M %p")
    except:
        return "06:00 AM", "06:00 PM"

def calculate_panchang(year, month, day, latitude=28.6139, longitude=77.2090, tz='Asia/Kolkata'):
    swe.set_topo(longitude, latitude, 0)
    jd = swe.julday(year, month, day)

    sun_long = swe.calc_ut(jd, swe.SUN)[0][0]
    moon_long = swe.calc_ut(jd, swe.MOON)[0][0]

    tithi_num = int(((moon_long - sun_long) % 360) / TITHI_SIZE)
    nakshatra_num = int((moon_long % 360) / NAKSHATRA_SIZE)
    yoga_num = int(((sun_long + moon_long) % 360) / YOGA_SIZE)

    weekday = weekday = datetime.date(year, month, day).strftime("%A")
    sunrise, sunset = get_sunrise_sunset(jd, latitude, longitude)
    tithi_end = jd + (TITHI_SIZE - ((moon_long - sun_long) % TITHI_SIZE)) / 13.2 / 24

    karana1, karana2 = get_karana_names(tithi_num)

    return {
        "date": f"{weekday}, {datetime.date(year, month, day).strftime('%B %d, %Y')}",
        "sunrise": sunrise,
        "sunset": sunset,
        "tithi": {
            "name": get_tithi_name(tithi_num),
            "ends": to_local_time(tithi_end).strftime("%I:%M %p")
        },
        "nakshatra": {
            "name": get_nakshatra_name(nakshatra_num),
            "ends": get_nakshatra_end(jd)
        },
        "yoga": {
            "name": get_yoga_name(yoga_num),
            "ends": "TBD"
        },
        "karana": [
  {"name": "Balava", "ends": "2025-08-21"},
            {"name": "Kaulava", "ends": "2025-08-21"}
        ],
        "paksha": "Shukla" if tithi_num < 15 else "Krishna",
        "weekday": weekday,
        "month": {
            "amanta": get_amanta_month(sun_long),
            "purnimanta": get_purnimanta_month(sun_long)
        },
        "moonsign": get_rashi(moon_long),
        "sunsign": get_rashi(sun_long),
        "pravishte": 14,
        "shaka_samvat": year - 78,
        "vikram_samvat": year + 57,
        "gujarati_samvat": year + 57
    }
