from brain_games.utils import get_random_number, get_random_choice
from brain_games.game_engine import game_engine
from brain_games.constants import PROGRESSION_LENGTH
from brain_games.constants import PROG_GAME_BRIEFING


def get_random_sequence_and_answer():
    random_step = get_random_number(5)
    start_number = get_random_number(15)
    sequence = []
    sequence.append(start_number)
    for i in range(PROGRESSION_LENGTH):
        sequence += [sequence[i] + random_step]
    missed_number = get_random_choice(sequence)
    question = ''
    for i in range(len(sequence)):
        question += ' ' + str(sequence[i]) if sequence[i] != missed_number else ' ..'
    return question.strip(), str(missed_number)


def progression_game():
    game_engine(get_random_sequence_and_answer, PROG_GAME_BRIEFING)
