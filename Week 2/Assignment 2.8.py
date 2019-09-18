## Name: Robert Kreml
## Date: September 11, 2019
## Class: EPSY 5200

## Exercise 8 from LP3TH by Zed Shaw

# The following line of code is creating a variable and placing four braces within it that can be filled with four strings if need be.
formatter = "{} {} {} {}"

# The following code prints out the formatter variable and replaces the four braces with '1 2 3 4'
print(formatter.format(1, 2, 3, 4))

# The following code prints out the formatter variable and replaces the four braces with 'one two three four'
print(formatter.format("one", "two", "three", "four"))

# The following code prints out the formatter variable and replaces the four braces with 'True False False True'
print(formatter.format(True, False, False, True))

# The following code prints out the formatter variable and replaces the four brades with four braces each. Therefore it prints out 16 sets of braces.
print(formatter.format(formatter, formatter, formatter, formatter))

# The following code prints out the following text onto a single line because despite the text being broken up into four short lines of text, it is still the formatter variable being four braces in a row to be replaces with the four lines of text.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

## Study Drills
# 1) Added the comments throughout the script as requested.
# 2) No errors that I can find.
# 3) Will do, and also will note them in the scripts below as I have been doing.
# 4) Will do.
# 5) Also, understand.

## Mistakes
# 1) No mistakes were made in this script to my knowledge.