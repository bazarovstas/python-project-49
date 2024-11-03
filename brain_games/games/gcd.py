import random

from brain_games.game_engine import game_engine
from brain_games.constants import GCD_GAME_INTRODUCTION


def get_greatest_common_divisor(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def get_random_numbers_and_answer():
    num1, num2 = random.randint(1, 101), random.randint(1, 101)
    question = f' {num1} {num2}'
    answer = str(get_greatest_common_divisor(num1, num2))
    return question, answer


def gcd_game():
    game_engine(get_random_numbers_and_answer, GCD_GAME_INTRODUCTION)
