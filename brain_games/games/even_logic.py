import random


MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True


def take_game():
    num = random.randint(1, 100)
    question = f'''Question: {num}'''
    if is_even(num):
        correct = "yes"
    else:
        correct = "no"
    return question, correct
