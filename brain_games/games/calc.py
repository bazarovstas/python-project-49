from random import choice
from brain_games.utils import get_random_num
from brain_games.game_engine import game_engine
from brain_games.constants import CALC_BRIEFING


def get_random_math_sym_and_answer(num1: int, num2: int) -> list[str | int]:
    return choice([
        ['+', num1 + num2],
        ['-', num1 - num2],
        ['*', num1 * num2],
    ])


def get_expression_and_answer():
    num1, num2 = get_random_num(max_range=15), get_random_num(max_range=10)
    random_math_symbol, answer = get_random_math_sym_and_answer(num1, num2)
    question = f'{num1} {random_math_symbol} {num2}'
    return question, str(answer)


def calc_game():
    game_engine(get_expression_and_answer, CALC_BRIEFING)
