## Name: Robert Kreml
## Date: September 23, 2019
## Class: EPSY 5200

## Exercise 19 from LP3TH by Zed Shaw

# this line is creating a new function called 'cheese_and_crackers' and defines two variables within the function: 'cheese_count', and 'boxes_of_crackers'.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # this line prints the following line with the amount of cheese_count as a number.
    print(f"You have {cheese_count} cheeses!")
    # this line prints the following line with the boxes of crackers as a number.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # this line prints out the following text in "".
    print("Man that's enough for a party!")
    # this line prints out 'Get a blanket' and then starts a new line.
    print("Get a blanket. \n")

# this line prints out the following text in "".
print("We can just give the function numbers directly:")
# this line assigns the values of 20 and 30 for cheese and crackers under the variable name.
cheese_and_crackers(20, 30)

# this line prints the following text in "".
print("OR, we can use variables from our script:")
# this line assigns numbers to the variable name.
amount_of_cheese = 10
# this line assigns numbers to the variable name.
amount_of_crackers = 50

# this line uses the first function we defined on line 8 and just uses the variable assignment on 26 and 28 to complete the function.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this line prints the text in the "".
print("We can even do math inside too:")
# this line uses functionon line 8 and just inputs numbers or summations for the two variables inside of the function.
cheese_and_crackers(10 + 20, 5 + 6)

# this line prints the text in the "".
print("And we can combine the two, variables and math:")
# this line uses the variable assignment we did on lines 26 and 28 and adds numbers to them to complete the function.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# this line prints the text in the "".
print("This is one of my own:")
# this line assigns a new value to amount_of_cheese.
amount_of_cheese = 1000
# this line assigns a new value to amount_of_crackers.
amount_of_crackers = 7
# this line uses the variable assignment just completed and adds/subtracts numbers to them to complete the function.
cheese_and_crackers(amount_of_cheese - 500, amount_of_crackers - 1)
# this line prints the text in the "".
print("I really like cheese.")

## Study Drills
# 1) Added in comments throughout.
# 2) Completed.
# 3) Added the new group and comments on lines 43 - 52

## Mistakes
# 1) No mistakes were made in this script from what I could tell.