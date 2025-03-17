# Guess a Random Number
# Author: M McMahon
# Using random

import random
number = random.randint(1, 10)
print(number)

found=0

x = input("Guess the Number: ")
while found == 0:
	if int(x) == number:
  		found=1
	else:
   		x = input("Sorry. Guess again: ")

# Output:
print ("Congratulations !")
