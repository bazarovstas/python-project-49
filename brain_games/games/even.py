import random
import prompt
import brain_games.constants as const
from brain_games.game_engine import game_engine


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_random_num_and_answer():
    number = random.randint(1, 101)
    even_check = is_even(number)
    return number, even_check


def even_game():
    # game_engine()

    username = prompt.string(''.join(const.GREETING))

    print(f'Hello, {username}!')
    print(''.join(const.EVEN_GAME_INTRODUCTION))

    for _ in range(const.GAMES_TO_WIN):
        number, even_check = get_random_num_and_answer()

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if even_check == answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{even_check}'.\n"
                f"Let's try again, {username}!"
            )
            return

    print(f'Congratulations, {username}!')
