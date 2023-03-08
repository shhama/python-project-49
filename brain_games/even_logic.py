import prompt
import random

def brain_even():
    dict = {True: "yes", False: "no"}
    count = 0
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        rand_num = random.randrange(100)
        correct_answ = dict[rand_num % 2 == 0]
        print(f'Question: {rand_num}')
        your_answ = prompt.string("Your answer: ")
        if your_answ == correct_answ:
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"{your_answ} is wrong answer ;(. Correct answer was {correct_answ}. Let's try again, {name}!")
            break

