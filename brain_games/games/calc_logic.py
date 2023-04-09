import random


MESSAGE = 'What is the result of the expression?'


FIRST_NUM = 1
LAST_NUM = 10
OPERATORS = ["+", "-", "*"]


def take_game():
    operand_first = random.randint(FIRST_NUM, LAST_NUM)
    operand_second = random.randint(FIRST_NUM, LAST_NUM)
    rand_op = random.choice(OPERATORS)
    actions = {
        "+": operand_first + operand_second,
        "-": operand_first - operand_second,
        "*": operand_first * operand_second
    }
    question = f'''Question: {operand_first} {rand_op} {operand_second}'''
    correct = str(actions[rand_op])
    return question, correct
