import random


def get_random_number(range: int = 100) -> int:
    random_number = random.randint(1, range)
    return random_number


def get_random_choice(collection: list[int]) -> int:
    random_choice = random.choice(collection)
    return random_choice
