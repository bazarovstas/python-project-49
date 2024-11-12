import random


def get_random_num(min_range: int = 1, max_range: int = 100) -> int:
    random_number = random.randint(min_range, max_range)
    return random_number
