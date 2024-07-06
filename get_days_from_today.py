from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    today_date = datetime.today().date()
    delta = today_date - given_date
    return delta.days

print(get_days_from_today("2024-07-20"))