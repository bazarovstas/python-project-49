import random

from brain_games.game_engine import game_engine
from brain_games.constants import PRIME_GAME_INTRODUCTION


def is_prime(number):
    if number == 1:
        return 'no'
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return 'yes' if number == divisor else 'no'


def get_random_number_and_answer():
    random_number = random.randint(1, 101)
    return str(random_number), is_prime(random_number)


def prime_game():
    game_engine(get_random_number_and_answer, PRIME_GAME_INTRODUCTION)
