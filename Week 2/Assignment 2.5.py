## Name: Robert Kreml
## Date: September 11, 2019
## Class: EPSY 5200

## Exercise 5 from LP3TH by Zed Shaw

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = (height * 2.54) # centimeters
weight = 180 # lbs
weight_kg = (weight * 0.453592) # Kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

## Study Drills
# 1) I have changed all of the variables to no longer include "my_" in all areas of the script.
# 2) I have added in the conversion for both height and weight in centimeters and kilograms respectively. Below is a print line to show the answer.

print(f"I have converted {name}'s height and weight into centimeters and Kilograms as requested in the second study drill.")
print(f"{name}'s weight in Kilograms is: {weight_kg}. {name}'s height in centimeters is: {height_cm}.")

## Mistakes
# 1) Added an extra "my" in line 15. Was corrected to make the sentence make sense. I learned to pay closer attention to what the book has written in it.