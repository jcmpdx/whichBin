import datetime

schedule = [0, 1, 0, 1, 0, 1, 0]  # 0 for yard debris, 1 for recycle

today = datetime.date.today()
current_weekday = today.weekday()  # Monday through Sunday is 0 through 6
days_until_next_monday = (7 - current_weekday) % 7
next_monday = today + datetime.timedelta(days=days_until_next_monday)

# https://strftime.org/ Python date format
if schedule[next_monday.day % len(schedule)] == 0:
    print(f"Next Monday ({next_monday.strftime('%b %d, %Y')}) is the YARD DEBRIS bin.")
else:
    print(f"Next Monday ({next_monday.strftime('%b %d, %Y')}) is the RECYCLE bin.")
