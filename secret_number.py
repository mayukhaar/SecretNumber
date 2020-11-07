print("GUESS THE SECRET NUMBER")
print("------------------------")

from random import randint

value = randint(0,10)
print ("random value is: " + str(value))
# change this later, Mayukha, Mayukha, CHANGEEEEE
num_tries = 0
random_num = value

# repeat part:
# print("Oops, your number was too small! Try again:)")
#     guess = input("Enter a number between 0 and 10:")
#     print("You guessed " + str(guess))
#     num_tries = num_tries + 1
#     print("Number of tries: " + str(num_tries))
#     if int(guess) > random_num:
#         print("Oops, your number was too big! Try again:)")
#         guess = input("Enter a number between 0 and 10:")
#         print("You guessed " + str(guess))
#         num_tries = num_tries + 1
#         print("Number of tries: " + str(num_tries))
#     elif int(guess) < random_num:
#         print("Oops, your number was too small! Try again:)")
#         guess = input("Enter a number between 0 and 10:")
#         print("You guessed " + str(guess))
#         num_tries = num_tries + 1
#         print("Number of tries: " + str(num_tries))
#     else:
#         play_again = input("You got it!")
#         print(num_tries)

guess = input("Enter a number between 0 and 10:")
print("You guessed " + str(guess))
num_tries = num_tries + 1
print("Number of tries: " + str(num_tries))
big_message = " Oops, your number was too big."
small_message = " Oops, your number was too small."

while int(guess) > random_num or int(guess) < random_num:
    if int(guess) > random_num:
         print(" Try again:)" + big_message)
    elif int(guess) < random_num:
        print(" Try again:)" + small_message)
    guess = input("Enter a number between 0 and 10:")
    print("You guessed " + str(guess))
    num_tries = num_tries + 1
    print("Number of tries: " + str(num_tries))
else:
    print("You got it!")


#         #when same number is repeated, make sure it doesn't count in the number of tries
