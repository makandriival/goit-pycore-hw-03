from datetime import datetime

def get_days_from_today(date):
    if not isinstance(date, str):
        return "Error: date must be a string in format YYYY-MM-DD."

    try:
        today = datetime.now().date()
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        delta = target_date - today
        return delta.days
    except ValueError:
        return "Error: invalid date format. Use YYYY-MM-DD."