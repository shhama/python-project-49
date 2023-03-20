#!/usr/bin/env python3
import prompt
import random


def is_nod(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return is_nod(a - b, b)
    else:
        return is_nod(a, b - a)


def gcd_game():
    count = 0
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    while count < 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f'Question: {a} {b}')
        your_answ = prompt.string("Your answer: ")
        if int(your_answ) == is_nod(a, b):
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'''{your_answ} is wrong answer ;(. Correct answer'''
                  f''' was {is_nod(a, b)}. \nLet's try again, {name}!''')
            break
