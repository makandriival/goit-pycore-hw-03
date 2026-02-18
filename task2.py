from random import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(int(random() * (max - min + 1)) + min)
    return sorted(numbers)

print(get_numbers_ticket(1, 100, 5))