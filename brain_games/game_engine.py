import prompt
import brain_games.constants as const


def game_engine(get_question_and_answer, introduction):
    username = prompt.string(''.join(const.GREETING))
    print(f'Hello, {username}!')
    print(''.join(introduction))
    for _ in range(const.GAMES_TO_WIN):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{answer}'.\n"
                f"Let's try again, {username}!"
            )
            return
    print(f'Congratulations, {username}!')
