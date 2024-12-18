from brain_games.utils import get_random_num
from brain_games.game_engine import game_engine
from brain_games.constants import EVEN_BRIEFING


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_random_num_and_answer():
    random_number = get_random_num()
    even_check = 'yes' if is_even(random_number) else 'no'
    return str(random_number), even_check


def even_game():
    game_engine(get_random_num_and_answer, EVEN_BRIEFING)
