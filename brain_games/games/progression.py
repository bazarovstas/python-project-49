from brain_games.utils import get_random_number, get_random_choice
from brain_games.game_engine import game_engine
from brain_games.constants import PROG_GAME_BRIEFING
# from brain_games.constants import STEP_OF_SEQUENCE


def get_random_sequence_and_answer():
    random_step = get_random_choice(['2', '3', '4'])
    start_number = get_random_number(15)
    sequence = []
    sequence.append(start_number)
    for i in range(8):
        sequence += [sequence[i] + random_step]
    question = ''
    answer = get_random_choice(sequence)
    for i in range(len(sequence)):
        question += ' ' + str(sequence[i]) if sequence[i] != answer else ' ..'
    return question.strip(), str(answer)


def progression_game():
    game_engine(get_random_sequence_and_answer, PROG_GAME_BRIEFING)
