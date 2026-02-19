# Вимоги до завдання:
# Параметр функції users — це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
# Рекомендації для виконання:
# Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт — datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
# Визначте поточну дату системи за допомогою datetime.today().date().
# Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
# Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
# Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
# Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
# Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
# Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань
from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    if not isinstance(users, list):
        return "Error: users must be a list of dictionaries."

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        if not isinstance(user, dict):
            return "Error: each user must be a dictionary with 'name' and 'birthday'."

        name = user.get("name")
        birthday_str = user.get("birthday")

        if not isinstance(name, str) or not isinstance(birthday_str, str):
            return "Error: each user must contain string fields 'name' and 'birthday'."

        try:
            birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        except ValueError:
            return "Error: birthday must be in YYYY.MM.DD format."

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:
                days_until_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_until_monday)
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays