import prompt
import random


def play_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        operand_first = random.randint(0, 10)
        operand_second = random.randint(0, 10)
        operators = ["+", "-", "*"]
        rand_op = random.choice(operator)
        expression = f'{operand_first} {rand_op} {operand_second}'
        dict = {
            "+": operand_first + operand_second,
            "-": operand_first - operand_second,
            "*": operand_first * operand_second
        }
        correct_answ = dict[rand_op]
        print(f'Question: {expression}')
        your_answ = prompt.string("Your answer: ")
        if int(your_answ) == (correct_answ):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'''"{your_answ}" is wrong answer ;(. Correct answer was'''
                  f'''"{correct_answ}".\nLet's try again, {name}!''')
            break
