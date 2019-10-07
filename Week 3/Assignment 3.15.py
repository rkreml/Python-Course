## Name: Robert Kreml
## Date: September 23, 2019
## Class: EPSY 5200

## Exercise 15 from LP3TH by Zed Shaw

# This line is importing the argv information from the system.
from sys import argv

# This line is telling the script to save the filename as the argv.
script, filename = argv

# This line is telling the script that the file is a txt file type and to open it.
txt = open(filename)

# This line is printing 'Here's your file {name}:' as entered in the run command.
print(f"Here's your file {filename}:")

# This line tells the script to print that it is reading the txt file.
print(txt.read())

# This line prints 'Type the filename again:'.
print("Type the filename again:")

# This line is asking for the input from user and will save inpute as 'file_again'.
file_again = input("> ")

# This line saves a 'txt_again' variable from opening user's input from last line.
txt_again = open(file_again)

# This line prints that it is reading the file.
print(txt_again.read())

# This line will close the 'txt' filename variable.
txt.close(filename)

# This line will close the 'txt_again' filename variable.
txt_again.close(filename)

# This line prints that your file was closed to the user.
print("Your file is closed.")

## Study Drills
# 1) Comments have been added as necessary.
# 2) I looked up some information on argv. It was slightly confusing.
# 3) I know this from R.
# 4) I got rid of it by commenting out.
# 5) Swapped comments on lines as requested. The sys to import argv is probably better because there is less user error when finding the file name you want.
# 6) Yes, I see the opening and closing features of python3.6.
# 7) Added to script.

## Mistakes
# 1) Figuring out close took a while.