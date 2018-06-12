import random

print('----------------------------------')
print('         Number guessing game')
print('----------------------------------')
print()

the_number = random.randint(0, 100)

guess_text = input('Guess the number between 0 and 100: ')
guess = int(guess_text)

while True:
    if guess == the_number:
        print("You guessed it")
        break

    else:
        if the_number < guess:
            guess_text = input('Number is smaller than {0} Guess again: '.format(guess))
            guess = int(guess_text)
        else:
            guess_text = input('Number is larger than {0}, Guess again: '.format(guess))
            guess = int(guess_text)