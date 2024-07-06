from datetime import datetime, timedelta



def get_upcoming_birthdays(users):
  today = datetime.today().date()
  upcoming_birthdays = []

  for user in users:
    birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    birthday_this_year = birthday.replace(year=today.year)

    if birthday_this_year < today:
      birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    delta = (birthday_this_year - today).days

    if 0 <= delta and delta <= 7:
      weekday = birthday_this_year.weekday()
      if weekday >= 5:
         days = 7 - weekday
         birthday_this_year += timedelta(days=days)

      upcoming_birthdays.append({
        "name": user["name"],
        "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
      })

  return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "John Smith", "birthday": "1990.07.07"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Doe", "birthday": "1990.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
