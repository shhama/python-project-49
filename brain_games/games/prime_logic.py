import random
import prompt


dict = {True: "yes", False: "no"}


def is_prime(x):
    simple = False
    i = 2
    for i in range(i, x):
        if x % i == 0:
            simple = True
    return simple


def prime_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        n = random.randint(1, 100)
        simple = False
        print(f'''Question: {n}''')
        your_answ = prompt.string("Your answer: ")
        simple = is_prime(n)
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
