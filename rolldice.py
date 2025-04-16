#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the the function is asked to generate
#3D6 or three sixed sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will as the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)

# How many dice to roll? 3
# How many sides? 6
# Here are the results: [6, 1, 6]

# How many dice to roll? 0
# How many sides? 5
# Error: Sides must be greater than 1 and dice count greater than 0.

# How many dice to roll? 20
# How many sides? 20
# Here are the results: [18, 19, 6, 8, 13, 6, 6, 6, 18, 12, 20, 10, 14, 8, 14, 17, 12, 15, 20, 17]

import random

# Get inputs from user about the dice

num_dice = int(input("How many dice do you want to roll?"))
num_sides = int(input("How many sides per die?"))

# Define the function to roll dice
def myFunctionDice(num_dice, num_sides):
    myList = []
    rolls = []
    for i in range(num_dice, num_sides):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

# Validate input (check if it is correct)

if num_dice <= 0 or num_sides <= 1:
    print("Error: sides and dice count are not valid.")
else:
    # Nothing wrong, call your function and print the result

    results = myFunctionDice(num_dice, num_sides)

results = myFunctionDice(3, 8) # Roll 7 dice
print("Here are the results:", results)
    
    

    