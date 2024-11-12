from brain_games.utils import get_random_number
from brain_games.game_engine import game_engine
from brain_games.constants import PROGRESSION_LENGTH
from brain_games.constants import PROG_GAME_BRIEFING


def get_random_sequence_and_answer():
    random_step = get_random_number(max_range=5)
    start_number = get_random_number(max_range=15)
    sequence = []
    sequence.append(start_number)
    for i in range(PROGRESSION_LENGTH):
        sequence += [sequence[i] + random_step]
    missed_num_index = get_random_number(min_range=0, max_range=len(sequence) - 1)
    question = ''
    for i in range(len(sequence)):
        question += ' ' + str(sequence[i]) if sequence[i] != missed_num_index else ' ..'
    return question.strip(), str(missed_num_index)


def progression_game():
    game_engine(get_random_sequence_and_answer, PROG_GAME_BRIEFING)
