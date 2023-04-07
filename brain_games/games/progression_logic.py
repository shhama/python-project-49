#!/usr/bin/env python3
import random


MESSAGE = "What number is missing in the progression?"


def make_progression():
    start = random.randint(1, 100)
    step = random.randint(1, 5)
    size = 10
    a = []
    for i in range(size):
        start += step
        i += start
        a.append(start)
    return a


def take_game():
    progression = make_progression()
    rand_int = random.randint(1, 9)
    string = [str(i) for i in progression]
    string[rand_int] = ".."
    join_strng = " ".join(string)
    question = f'''Question: {join_strng}'''
    correct = str(progression[rand_int])
    return question, correct
