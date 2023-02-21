import random
print('I am thinking of a number between 1-20, can you guess it? ')
target_number = random.randint(1,20)
count = 0


while count < 5:
    user_guess = int(input())
    if user_guess < target_number:
        print('Your guess is too low, guess again')
        count = count +  1
    elif user_guess > target_number:
        print('Your guess is too high, guess again')
        count = count +  1
    else:
        break

if target_number == user_guess:
    print('Perfect! You guessed the right number in ' + str(count) + ' tries!')
else:
    print('The actual number was ' + str(count))
print('Thanks for playing!')
