
import datetime
import json
from panchang.calculator import calculate_panchang
from panchang.db import save_panchang, init_db

def precompute():
    init_db()
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=1460)  # 4 years

    for i in range((end_date - start_date).days + 1):
        current_date = start_date + datetime.timedelta(days=i)
        print(f"Computing: {current_date}")
        data = calculate_panchang(current_date.year, current_date.month, current_date.day)
        save_panchang(current_date.isoformat(), json.dumps(data))

if __name__ == "__main__":
    precompute()
