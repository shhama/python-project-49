import prompt
from random import randint


BEGIN = 1
END = 100
dictval = {True: 'yes', False: 'no'}


def even_play():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = randint(BEGIN, END)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        coorect = dictval[num % 2 == 0]
        if answer != coorect:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "{coorect}".\n Let's try again, {name}!''')
            break
        else:
          print('Correct')
          count += 1
    if count == 3:
        print(f'Congratulations, {name}!')

