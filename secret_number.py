print("GUESS THE SECRET NUMBER")
print("------------------------")
from random import randint

value = randint(0,10)
print ("random value is: " + str(value))
# change this later, Mayukha, Mayukha, CHANGEEEEE
num_tries = 0
random_num = value
guess = input("Enter a number between 0 and 10:")
print("You guessed " + str(guess))
num_tries = num_tries + 1
print("Number of tries: " + str(num_tries))
if int(guess) > random_num:
    print("Oops, your number was too big! Try again:)")
    # add something to continue guessing
    #mark how many tries it took
elif int(guess) < random_num:
    print("Oops, your number was too small! Try again:)")
    # add something to continue guessing
    #mark how many tries it took
else:
    play_again = input("You got it! Do you want to play again? (yes/no)")
    if play_again = "yes":
        
    print(play_again)
    # if random_num is greater than generated number:
    # print("Oops, your number was too big! Try again:)")
    # elif num is less than generated number:
    # print("Oops, your number was too small... try again:)")
    # else:
    # print("You got it! YAY! Do you want to play again?")