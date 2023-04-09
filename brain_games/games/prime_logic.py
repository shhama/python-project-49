import random


ACTIONS = {True: "yes", False: "no"}
MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    simple = True
    a = 2
    for i in range(a, x):
        if x % i == 0:
            simple = False
    return simple


def take_game():
    n = random.randint(1, 100)
    question = f'''Question: {n}'''
    simple = is_prime(n)
    correct = ACTIONS[simple]
    return question, correct
