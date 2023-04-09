import prompt


ATTEMPTS = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May i have your name? ")
    print(f'''Hello, {name}!''')
    print(game.MESSAGE)
    tries = ATTEMPTS
    while tries:
        question, correct = game.take_game()
        print(question)
        answer = prompt.string("Your answer: ")
        if answer != correct:
            print(f'''"{answer}" is wrong answer ;(.'''
                  f''' Correct answer was "{correct}".''')
            print(f'''Let's try again, {name}!''')
            return
        else:
            print("Correct!")
            tries -= 1
    print(f'''Congratulations, {name}!''')
