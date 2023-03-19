#!/usr/bin/env python3

import random
import prompt
import string


def arithmet_progr():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(f'What number is missing in the progression?')
    count = 0
    while count < 3:
        start = random.randint(1, 100)
        step = random.randint(1, 5)
        size = 10
        a = []
        for i in range(size):
            start += step
            i += start
            a.append(start)
        rand_int = random.randint(1, 9)
        string = [str(i) for i in a]
        string[rand_int] = ".."
        join_strng = " ".join(string)
        print(f'''Question: {join_strng}''')
        your_answ = prompt.string("Your answer: ")
        if int(your_answ) != a[rand_int]:
            print(f''''{your_answ}' is wrong answer ;(. Correct answer was '{a[rand_int]}'.\nLet's try again, {name}!"''')
            break
        else:
            print("Correct!")
       	    count += 1
            if count == 3:
                print(f'''Congratulations, {name}!''')
