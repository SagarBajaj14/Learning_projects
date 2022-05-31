import random

top_range = input(" Enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range<=0:
        print(" Please enter a number greater than 0 ")
        quit()

else:
    print(" Please enter a number next time. ")
    quit()

rand_num = random.randint(0,top_range)
guesses = 5


while guesses > 0 :
    user_guess = input(" Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print(" Please enter a number next time. ")
        continue

    if user_guess == rand_num:
        print(" Yay! You got it. ")
        break
    else:
        if user_guess > rand_num:
            print(" You were above the number!")
        else:
            print(" You were below the number!")
        guesses-=1
        print(" You got ", guesses, " guesses left ")

if guesses == 0 and user_guess!=rand_num:
    print("\n You lost ! Better luck next time :)")











