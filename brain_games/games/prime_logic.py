import random
import prompt


def is_prime():
    dict = {True: "yes", False: "no"}
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        simple = True
        n = random.randint(1, 100)
        print(f'''Question: {n}''')
        your_answ = prompt.string("Your answer: ")
        i = 2
        for i in range(i, n):
            if n % i == 0:
                simple = False
        correct_answ = dict[simple]
        if your_answ != correct_answ:
            print(f'''"{your_answ}" is wrong answer ;(. Correct answer was'''
                  f'''" {correct_answ}". Let's try again, {name}!''')
            break
        else:
            print('Correct!')
        count += 1
        if count == 3:
            print(f'''Congratulations, {name}!''')
