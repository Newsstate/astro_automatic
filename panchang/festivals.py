from datetime import timedelta
from panchang.festival_calculator import calculate_festival_days, get_masik_shivratri
from panchang.festival_calculator import get_masik_shivratri

from panchang.festival_calculator import get_ekadashis




def make_festival(date_obj, name, panchang):
    return {
        "date": date_obj.isoformat(),
        "readable_date": date_obj.strftime("%B %d, %Y"),
        "name": name,
        "tithi": panchang["tithi"]["name"],
        "paksha": panchang["paksha"],
        "month": panchang["month"]["purnimanta"],
        "weekday": panchang["weekday"]
    }

def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    return festivalsy


def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya
)

def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat
)

def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods
)


def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi  # ✅ NEW
)



def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)  # ✅ NEW
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi,
    get_kalashtami  # ✅ NEW
)




def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)
    festivals += get_kalashtami(start, end)  # ✅ NEW
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi,
    get_kalashtami,
    get_masik_krishna_janmashtami  # ✅ NEW
)



def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)
    festivals += get_kalashtami(start, end)
    festivals += get_masik_krishna_janmashtami(start, end)  # ✅ NEW
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi,
    get_kalashtami,
    get_masik_krishna_janmashtami,
    get_rohini_vrat  # ✅ new line
)


def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)
    festivals += get_kalashtami(start, end)
    festivals += get_masik_krishna_janmashtami(start, end)
    festivals += get_rohini_vrat(start, end)  # ✅ NEW
    return festivals



from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi,
    get_kalashtami,
    get_masik_krishna_janmashtami,
    get_rohini_vrat,
    get_masik_karthigai  # ✅ NEW
)


def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)
    festivals += get_kalashtami(start, end)
    festivals += get_masik_krishna_janmashtami(start, end)
    festivals += get_rohini_vrat(start, end)
    festivals += get_masik_karthigai(start, end)  # ✅ NEW
    return festivals



from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi,
    get_kalashtami,
    get_masik_krishna_janmashtami,
    get_rohini_vrat,
    get_masik_karthigai,
    get_darsha_anvadhan_ishti  # ✅ new
)


   # Make sure this line starts with NO spaces or tabs
def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)
    festivals += get_kalashtami(start, end)
    festivals += get_masik_krishna_janmashtami(start, end)
    festivals += get_rohini_vrat(start, end)
    festivals += get_masik_karthigai(start, end)
    festivals += get_darsha_anvadhan_ishti(start, end)
    return festivals


from panchang.festival_calculator import (
    calculate_festival_days,
    get_masik_shivratri,
    get_masik_durgashtami,
    get_monthly_purnima_amavasya,  # ✅ correct name
    get_pradosh_vrat,
    get_navratri_periods,
    get_sankashti_chaturthi,
    get_kalashtami,
    get_masik_krishna_janmashtami,
    get_rohini_vrat,
    get_masik_karthigai,
    get_darsha_anvadhan_ishti,
    get_sankrantis,
    get_ekadashis,
    get_vasant_panchami,
    get_ratha_saptami,
    get_bhishma_ashtami,
    get_nag_panchami,
    get_raksha_bandhan,
    get_pitru_paksha_start,
    get_varalakshmi_vratam,
    get_ganga_dussehra,
    get_vaibhav_lakshmi_vrat,
)




def calculate_festivals(start, end):
    festivals = []
    festivals += calculate_festival_days(start, end)
    festivals += get_masik_shivratri(start, end)
    festivals += get_masik_durgashtami(start, end)
    festivals += get_monthly_purnima_amavasya(start, end)
    festivals += get_pradosh_vrat(start, end)
    festivals += get_navratri_periods(start, end)
    festivals += get_sankashti_chaturthi(start, end)
    festivals += get_kalashtami(start, end)
    festivals += get_masik_krishna_janmashtami(start, end)
    festivals += get_rohini_vrat(start, end)
    festivals += get_masik_karthigai(start, end)
    festivals += get_darsha_anvadhan_ishti(start, end)
    festivals += get_sankrantis(start, end)  # ✅ new
    festivals += get_ekadashis(start, end)   
    festivals += get_vasant_panchami(start, end)
    festivals += get_ratha_saptami(start, end)
    festivals += get_bhishma_ashtami(start, end)
    festivals += get_nag_panchami(start, end)
    festivals += get_raksha_bandhan(start, end)
    festivals += get_pitru_paksha_start(start, end)
    festivals += get_varalakshmi_vratam(start, end)
    festivals += get_ganga_dussehra(start, end)
    festivals += get_vaibhav_lakshmi_vrat(start, end)
    return festivals










