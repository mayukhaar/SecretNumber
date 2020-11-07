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
    guess = input("Enter a number between 0 and 10:")
    print("You guessed " + str(guess))
    num_tries = num_tries + 1
    print("Number of tries: " + str(num_tries))
elif int(guess) < random_num:
    print("Oops, your number was too small! Try again:)")
    guess = input("Enter a number between 0 and 10:")
    print("You guessed " + str(guess))
    num_tries = num_tries + 1
    print("Number of tries: " + str(num_tries))
else:
    play_again = input("You got it!")
    print(num_tries)

    if play_again == "yes":
        print(play_again)

    else:
        print("Bye. Have a great day!! :D ")


        #figure out how to repeat game
        #number of tries increase with game
