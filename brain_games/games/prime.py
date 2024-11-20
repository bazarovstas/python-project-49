from brain_games.utils import get_random_num
from brain_games.game_engine import game_engine
from brain_games.constants import PRIME_BRIEFING


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def get_random_number_and_answer():
    random_number = get_random_num()
    prime_check = 'yes' if is_prime(random_number) else 'no'
    return str(random_number), prime_check


def prime_game():
    game_engine(get_random_number_and_answer, PRIME_BRIEFING)
