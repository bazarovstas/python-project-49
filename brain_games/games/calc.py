import random
from brain_games.game_engine import game_engine
from brain_games.constants import MATH_SYMBOLS
from brain_games.constants import CALC_GAME_BRIEFING


def get_expression_and_answer():
    num1, num2 = random.randint(1, 21), random.randint(1, 11)
    random_symbol = random.choice(MATH_SYMBOLS)
    expression = f'{str(num1)} {random_symbol} {str(num2)}'
    answer = str(eval(expression))
    return expression, answer


def calc_game():
    game_engine(get_expression_and_answer, CALC_GAME_BRIEFING)
