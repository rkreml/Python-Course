## Name: Robert Kreml
## Date: September 23, 2019
## Class: EPSY 5200

## Exercise 16 from LP3TH by Zed Shaw

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(line1, "\n", line2, "\n", line3, "\n")

print("And finally, we close it.")
target.close()

## Study Drills
# 1) I have an idea what this all does.
# 2) I will attach the script as 'Assignment 3.16.a.py'
# 3) This is completed, I commented out the old multiple line method.
# 4) You need to explicitly tell python to have write permissions. It is old chmod style. It defaults to read only.
# 5) Yes you still need it because it defaults to read only even with truncate.

## Mistakes
# 1) No mistakes were made in this script from what I could tell.