from brain_games.utils import get_random_number, get_random_choice
from brain_games.game_engine import game_engine
from brain_games.constants import MATH_SYMBOLS
from brain_games.constants import CALC_GAME_BRIEFING


def get_expression_and_answer():
    num1, num2 = get_random_number(20), get_random_number(10)

    random_symbol = get_random_choice(MATH_SYMBOLS)
    expression = f'{str(num1)} {random_symbol} {str(num2)}'
    answer = str(eval(expression))
    return expression, answer


def calc_game():
    game_engine(get_expression_and_answer, CALC_GAME_BRIEFING)
