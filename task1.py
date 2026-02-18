from datetime import datetime

def get_days_from_today(date):

    today = datetime.now().date()
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    delta = target_date - today
    return delta.days

print(get_days_from_today("2023-10-09"))