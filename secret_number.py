print("GUESS THE SECRET NUMBER")
print("------------------------")

from random import randint

value = randint(0,10)
print ("random value is: " + str(value))
# change this later, Mayukha, Mayukha, CHANGEEEEE
num_tries = 0
random_num = value

list_1 = [1,2,3,4,5,6,7,8,9,1]
print(list_1)
len(list_1)
print(len(list_1))
list_2 = list(dict.fromkeys(list_1))
print(list_2)
len(list_2)
print(len(list_2))

lst_guess = []
final_list = []

guess = input("Enter a number between 0 and 10:")
print("You guessed " + str(guess))

num_tries = num_tries + 1
print("Number of tries: " + str(num_tries))
big_message = " Oops, your number was too big."
small_message = " Oops, your number was too small."

while int(guess) > random_num or int(guess) < random_num:
    lst_guess.append(guess)
    print("list value is" + str(lst_guess))
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
    final_list = list(dict.fromkeys(lst_guess))
    print("The number of tries is " + str(len(final_list)))

#         #when same number is repeated, make sure it doesn't count in the number of tries
