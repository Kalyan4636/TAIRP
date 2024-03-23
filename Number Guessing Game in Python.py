import random

def main():
    print('Number Guessing Game')
    print('--------------------')

    min_number = 1
    max_number = 100
    number_to_guess = random.randint(min_number, max_number)

    while True:
        guess = int(input(f'Enter your guess between {min_number} and {max_number}: '))

        if guess < number_to_guess:
            print('Too low! Try again.')
        elif guess > number_to_guess:
            print('Too high! Try again.')
        else:
            print('Congratulations! You guessed the number!')
            break

if __name__ == '__main__':
    main()
