## Name: Robert Kreml
## Date: September 11, 2019
## Class: EPSY 5200

## Exercise 6 from LP3TH by Zed Shaw

# This line is creating a new variable called 'types_of_people' and assigning it a value of 10.
types_of_people = 10

# This line is creating a new variable called 'x' and assigning it a string of characters and utilizing the variable 'types_of_people'.
# What is important here is that because a variable is being used, the 'f' has to be used at the beginning of the character and variable string. Good lesson to know!
x = f"There are {types_of_people} types of people."

# This line is creating a new variable called 'binary' and assigning it the value of a character string called 'binary'.
binary = "binary"

# This line is creating a new variable called 'do_not' and assigning it the value of a character string called 'don't'.
do_not = "don't"

# This line is creating a new variable called 'y' and assigning it the character and variable strings we just used. Again, has to use the 'f' before the start of the string as a variable is being used.
y = f"Those who know {binary} and those who {do_not}."

# This line is printing the variable assignment of 'x' into the terminal. So it shows "There are 10 types of people." when the script is ran.
print(x)

# This line is printing the variable assignment of 'y' into the terminal. So it shows "Those who know binary and those who don't." when the script is ran.
print(y)

# This line is printing a character and variable string into terminal when ran. Again, because there are variables, the 'f' needs to come before the string. When ran, this line should print "I said: There are 10 types of people.".
print(f"I said: {x}")

# This line is printing a character and variable string into terminal when the script is ran. Again, needs the 'f' before the string. When ran, this line should print "I also said: 'Those who know binary and those who don't.'".
print(f"I also said: '{y}'")

# This line is a variable assignment for 'hilarious' and setting the assignment to the logical variable of 'False'.
hilarious = False

# This line is creating a new variable called 'joke_evaluation' and assigning it to the character string 'Isn't that joke so funny?! {}'. What is important here is the braces at the end which allows for the combination of the two variables through the + sign in the print function.
# Without the {} at the end of this, the variable of 'hilarious' could not be used in the next line of code. It would just print 'joke_evaluation'.
joke_evaluation = "Isn't that joke so funny?! {}"

# This line is printing the variable 'joke_evaluation' into terminal and adding in the format of the 'hilarious' variable to the end in place of the {} in 'joke_evaluation'.
print(joke_evaluation.format(hilarious))

# This line is creating a new variable called 'w' and assigning a character string to it.
w = "This is the left side of..."

# This line is creating a new variable called 'e' and assigning a character string to it.
e = "a string with a right side."

# This line is printing the combination of variables 'w' and 'e' through the addition sign. This allows for two variables to be printed in sequence.
print(w + e)

## Study Drills
# 1) The comments have been added into the script.
# 2) There are strings inside of a string on lines 21 (twice), 30, & 33.
# 3) There are only four because a string is characterized by singe or double quotation marks around the variable or line. So a string within a string would need quotes around the thing being inserted inside quotes. Since hilarious does not have quotes, line 40 is not a string within a string.
# 4) The '+' allows for the two strings to be printed in sequence of each other.

## Mistakes
# 1) Missing a capital 'T' on line 46. Fixed. It is so difficult to copy the script from the book sometimes even given how careful I am.