import random
import prompt


def mk_progression():
    start = random.randint(1, 100)
    step = random.randint(1, 5)
    SIZE = 10
    a = []
    for i in range(SIZE):
        start += step
        i += start
        a.append(start)
    return a


def arithmet_progr():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        rand_int = random.randint(1, 9)
        a = mk_progression()
        string = [str(i) for i in a]
        string[rand_int] = ".."
        join_strng = " ".join(string)
        print(f'''Question: {join_strng}''')
        your_answ = prompt.string("Your answer: ")
        if int(your_answ) != a[rand_int]:
            print(f''''{your_answ}' is wrong answer ;(. Correct answer was'''
                  f''' {a[rand_int]}'.\nLet's try again, {name}!"''')
            break
        else:
            print("Correct!")
            count += 1
            if count == 3:
                print(f'''Congratulations, {name}!''')
