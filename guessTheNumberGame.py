import random 

secretNumber = random.randint(1,20)
print('I m thinking of a number between 1 to 20')

for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('The guess is too low')
    elif guess > secretNumber:
        print('The guess is too high')
    else:
        break 
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + 'attempts')
else:
    print('Nope. The number i was thinking of was ' + str(secretNumber))                 