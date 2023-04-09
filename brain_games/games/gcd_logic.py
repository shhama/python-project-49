import random


FIRST_NUM = 0
LAST_NUM = 10
MESSAGE = "Find the greatest common divisor of given numbers."


def is_nod(a, b):
    if a == 0 or b == 0:
        return str(a + b)
    if a > b:
        return str(is_nod(a - b, b))
    else:
        return str(is_nod(a, b - a))


def take_game():
    a = random.randint(FIRST_NUM, LAST_NUM)
    b = random.randint(FIRST_NUM, LAST_NUM)
    question = f'''Question: {a} {b}'''
    correct = is_nod(a, b)
    return question, correct
