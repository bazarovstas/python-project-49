import random

from brain_games.game_engine import game_engine
# from brain_games.constants import STEP_OF_SEQUENCE
from brain_games.constants import PROG_GAME_BRIEFING


def get_random_sequence_and_answer():
    random_step = random.choice(STEP_OF_SEQUENCE)
    start_number = random.randint(1, 16)
    sequence = []
    sequence.append(start_number)
    for i in range(8):
        sequence += [sequence[i] + random_step]
    question = ''
    answer = random.choice(sequence)
    for i in range(len(sequence)):
        question += ' ' + str(sequence[i]) if sequence[i] != answer else ' ..'
    return question.strip(), str(answer)


def progression_game():
    game_engine(get_random_sequence_and_answer, PROG_GAME_BRIEFING)
