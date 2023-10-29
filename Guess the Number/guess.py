import random

def guess(x):
    randomNumber = random.randint(1, x)
    num = 0
    while (num != randomNumber):
        num = int(input(f'Guess the Number between 1 to {x}: '))
        if (num < randomNumber):
            print('Sorry, Guess again. Too low.' )
        elif (num > randomNumber):
            print('Sorry, Guess again. Too high.')
        
    print(f'Congrats, You guessed right number {randomNumber}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while (feedback != 'c' and low != high):
        guessNum = random.randint(low, high)
        feedback = input(f'Is {guessNum} too high (H), too low(L), or correct(C): ')
        if (feedback == 'h'):
            high = guessNum - 1
        elif (feedback == 'l'):
            low = guessNum + 1

    print(f'Yay! The computer guessed your number, {guessNum}, correctly!')


computer_guess(10)   
