from random import randint

number = randint(1, 50)
shots = 0
guess_list = [0]

while True:
    guess = int(input('So your lucky number for today is: '))

    shots += 1

    if guess < 0 or guess > 50:
        print('OUT OF BOUNDS')
        continue

    # Add the wrong answers to list:
    guess_list.append(guess)
    print(guess_list)

    # if the answer is True:
    if guess == number and shots == 1:
        print('Correct! You got it after just 1 time!')
        break
    if guess == number and shots > 1:
        print('Correct! You got it after just', shots, 'times!')
        break

    # If the answer is False
    if 0 < abs(guess - number) <= 10 and shots == 1:
        print('WARM!')
    elif abs(guess - number) > 10 and shots == 1:
        print('COLD!')
    elif abs(guess - number) > abs(guess_list[-2] - number) and shots > 1:
        print('COLDER!')
    elif abs(guess - number) <= abs(guess_list[-2] - number) and shots > 1:
        print('WARMER!')

