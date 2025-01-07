from datetime import datetime, date
import re

def get_days_from_today(date):
    try:
        now_date = datetime.now()
        past_date = datetime.strptime(date, "%Y-%m-%d")
        differnce = (now_date-past_date).days
        return differnce
    except:
        print("Wrong format of date")


date = input("Print the date, days from wich you whant to count (РРРР-ММ-ДД): ")
print(get_days_from_today(date))