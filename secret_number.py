print("GUESS THE SECRET NUMBER")
print("------------------------")

from random import randint

value = randint(0,10)
# print ("random value is: " + str(value))
# change this later, Mayukha, Mayukha, CHANGEEEEE

random_num = value

lst_guess = []
final_list = []

guess = input("Enter a number between 0 and 10:")
print("You guessed " + str(guess))

big_message = " Oops, your number was too big."
small_message = " Oops, your number was too small."

while int(guess) > random_num or int(guess) < random_num:
    lst_guess.append(guess)
   # print("list value is" + str(lst_guess))
    if int(guess) > random_num:
         print(" Try again:)" + big_message)
    elif int(guess) < random_num:
        print(" Try again:)" + small_message)
    guess = input("Enter a number between 0 and 10:")
    print("You guessed " + str(guess))
else:
    print("You got it!")
    lst_guess.append(guess)
    final_list = list(dict.fromkeys(lst_guess))
    print("Number of tries: " + str(len(final_list)))

#         #when same number is repeated, make sure it doesn't count in the number of tries
