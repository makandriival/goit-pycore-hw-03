
# Вимоги до завдання:
# Параметр функції phone_number — це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду (додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.

import re

def normalize_phone(phone_number):
    normalized = re.sub(r"[^\d+]", "", phone_number)

    if not normalized.startswith('+'):
        if normalized.startswith('380'):
            normalized = '+' + normalized
        else:
            normalized = '+38' + normalized

    return normalized

print(normalize_phone("    +38(050)123-32-34"))  # Виведе: +380501233234
print(normalize_phone("     0503451234"))        # Виведе: +380503451234
print(normalize_phone("(050)8889900"))           # Виведе: +380508889900
print(normalize_phone("38050-111-22-22"))        # Виведе: +380501112222
print(normalize_phone("38050 111 22 11   "))      # Виведе: +380501112211