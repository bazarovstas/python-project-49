import random
import prompt

# ## Примерный алгоритм

# 1. Приветствуем пользователя сообщением, записываем имя в переменную
# 2. Генерируем число и правильный ответ
# 3. Выводим первое число, пользователь вводит ответ
# 4. отправляем ответ на проверку
# 5. если ответ верный, продолжаем игру, выводим второе число
# если ответ неверный, выводим сообщение и завершаем игру
# 6. после трех раундов выводим сообщение пользователю и завершаем игру
# 7. переходим к следующей игре


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_random_num_and_answer():
    number = random.randint(1, 101)
    even_check = is_even(number)
    return number, even_check


def even_game():

    username = prompt.string(
        'Welcome to the Brain Games!\n'
        'May I have your name? '
    )
    print(f'Hello, {username}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    GAMES_TO_WIN = 3

    for _ in range(GAMES_TO_WIN):
        number, even_check = get_random_num_and_answer()

        # print(number, even_check)

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
