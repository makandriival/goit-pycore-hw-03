from random import random


def get_numbers_ticket(min, max, quantity):
    if not all(isinstance(value, int) for value in (min, max, quantity)):
        return "Error: min, max, and quantity must be integers."

    if min < 1 or max > 1000 or min > max:
        return "Error: min and max must satisfy 1 <= min <= max <= 1000."

    if quantity < 1 or quantity > (max - min + 1):
        return "Error: quantity must be between 1 and the size of the selected range."

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(int(random() * (max - min + 1)) + min)
    return sorted(numbers)