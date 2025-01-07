from datetime import datetime, date
import re

def get_days_from_today(date):
    if re.match(r"(\d{4})-(\d{2})-(\d{2})", date):
        now_date = datetime.now()
        past_date = datetime.strptime(date, "%Y-%m-%d")
        differnce = (now_date-past_date).days
        print(differnce)
    else:
        print("Wrong format of date")
    return 0

date = input("Print the date, days from wich you whant to count (РРРР-ММ-ДД): ")
get_days_from_today(date)