from math import gcd
from brain_games.utils import get_random_num
from brain_games.game_engine import game_engine
from brain_games.constants import GCD_BRIEFING


def get_random_numbers_and_answer():
    num1, num2 = get_random_num(), get_random_num()
    question = f'{num1} {num2}'
    answer = gcd(num1, num2)
    return question, str(answer)


def gcd_game():
    game_engine(get_random_numbers_and_answer, GCD_BRIEFING)
