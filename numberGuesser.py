#randomly select number

import random


#tell the user to pick a number

guess = int(input("I am think of a number between 1 and 50, Guess what number "))


#selecting the number

num = random.randint(1,50) 

#prints if you got it right

if num == (guess):
    print("Yes you go it! You rock.")

else:
    print("WRONG! I was thinking of", num, "Try again! Better luck next time.")
