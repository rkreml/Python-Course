## Name: Robert Kreml
## Date: October 1, 2019
## Class: EPSY 5200

## Exercise 30 from LP3TH by Zed Shaw

people = 30
cars = 40
trucks = 15

# First checks to see if cars is greater than people, if so it prints the first line, if not then it checks if cars are less than people, then prints second if true. If cars is equal to people it will print the else statement.
if cars > people:
    print("WE should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# First checks to see if trucks is greater than cars, if so it prints the first line, if not then it checks if trucks are less than cars, then prints second if true. If trucks is equal to cars it will print the else statement.
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

# First checks to see if people is greater than trucks, if so it prints the first line, if not then it will print the else statement.
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# First checks to see if both people is equal to cars and cars are equal to trucks, if so it prints the first line. Otherwise, it will print the else statement.
if people == cars and cars == trucks:
    print("We can choose either and be fine!")
else:
    print("We have to pick one, or the other.")

## Study Drills
# 1) Elif is if the first if statement is false, it checks a new condition, if the elif is also false the else statement prints as the fail-safe.
# 2) Changed the values and then put them back to normal to check my logic. I was correct.
# 3) Added in an and statement.
# 4) Added comments above each of the logic statements.

## Mistakes
# 1) There were no mistakes in this script to my knowledge.