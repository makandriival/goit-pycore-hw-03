
# Вимоги до завдання:
# Параметр функції phone_number — це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду (додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.

import re

def normalize_phone(phone_number):
    if not isinstance(phone_number, str):
        return "Error: phone_number must be a string."

    normalized = re.sub(r"[^\d+]", "", phone_number)

    if not normalized:
        return "Error: phone number must contain digits."

    if not normalized.startswith('+'):
        if normalized.startswith('380'):
            normalized = '+' + normalized
        else:
            normalized = '+38' + normalized

    return normalized