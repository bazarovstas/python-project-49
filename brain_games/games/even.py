import random
from brain_games.game_engine import game_engine
from brain_games.constants import EVEN_GAME_BRIEFING


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_random_num_and_answer():
    random_number = random.randint(1, 101)
    even_check = is_even(random_number)
    return random_number, even_check


def even_game():
    game_engine(get_random_num_and_answer, EVEN_GAME_BRIEFING)
