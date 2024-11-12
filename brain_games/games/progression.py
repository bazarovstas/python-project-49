from random import choice
from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine
from brain_games.constants import PROGRESSION_LENGTH
from brain_games.constants import PROG_BRIEFING


def get_random_sequence_and_answer():
    random_step = get_random_number(min_range=2, max_range=5)
    start_number = get_random_number(max_range=15)
    seq = []
    seq.append(start_number)
    for i in range(PROGRESSION_LENGTH):
        seq += [seq[i] + random_step]
    missed_index = choice(seq)
    question = ''
    for i in range(len(seq)):
        print(seq[i])
        question += ' ' + str(seq[i]) if seq[i] != missed_index else ' ..'
    return question.strip(), str(missed_index)


def progression_game():
    game_engine(get_random_sequence_and_answer, PROG_BRIEFING)
