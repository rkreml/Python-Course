## Name: Robert Kreml
## Date: October 6, 2019
## Class: EPSY 5200

## Exercise 32 from LP3TH by Zed Shaw

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

## Study Drills
# 1) I looked up the range function and understand what it does.
# 2) I guess you could have if you already defined the variable with a range of 0,6 and then appended elements with those numbers. The print would be removed of course too.
# 3) Things like clear, copy, count, extend, index, insert, pop, remove, reverse, sort, etc.

## Mistakes
# 1) I messed up the second for statement by formatting the print statement to include 'fruits' not 'fruit'.