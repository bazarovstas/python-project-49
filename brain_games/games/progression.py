import random

from brain_games.game_engine import game_engine
from brain_games.constants import STEP_OF_SEQUENCE
from brain_games.constants import PROG_GAME_INTRODUCTION


def get_random_sequence_and_answer():
    sequence = []
    random_step = random.choice(STEP_OF_SEQUENCE)

    for i in range(8):
        if i == 0:
            sequence.append(random.randint(1, 16))
        else:
            sequence += [sequence[i-1] + random_step]

    question = ''
    answer = random.choice(sequence)

    for i in range(len(sequence)):
        if sequence[i] == answer:
            question += ' ..'
        else:
            question += ' ' + str(sequence[i])

    return question.strip(), str(answer)


def progression_game():
    game_engine(get_random_sequence_and_answer, PROG_GAME_INTRODUCTION)
