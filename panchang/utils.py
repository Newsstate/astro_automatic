
from datetime import datetime, timedelta
import pytz

def get_sunrise_sunset(latitude, longitude, date_obj):
    # Stub method — you can replace this with proper solar calc
    # Currently just returns dummy times
    sunrise = datetime.combine(date_obj, datetime.min.time()) + timedelta(hours=6)
    sunset = datetime.combine(date_obj, datetime.min.time()) + timedelta(hours=18)
    return sunrise.strftime('%H:%M'), sunset.strftime('%H:%M')
