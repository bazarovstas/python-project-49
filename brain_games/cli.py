import prompt


def welcome_user():
    username = prompt.string(
        'Welcome to the Brain Games!\n'
        'May I have your name? '
    )
    print(f'Hello, {username}!')
    return username
