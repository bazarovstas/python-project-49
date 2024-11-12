from brain_games.utils import get_random_num
from brain_games.game_engine import game_engine
from brain_games.constants import PRIME_BRIEFING


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    if number % 2 == 0:
        return number == 2
    square_root = int(number ** 0.5) + 1
    for divisor in range(3, square_root, 2):
        if number % divisor == 0:
            return False
    return True


def get_random_number_and_answer():
    random_number = get_random_num()
    prime_check = 'yes' if is_prime(random_number) else 'no'
    return str(random_number), prime_check


def prime_game():
    game_engine(get_random_number_and_answer, PRIME_BRIEFING)
