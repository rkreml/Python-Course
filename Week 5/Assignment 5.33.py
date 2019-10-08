## Name: Robert Kreml
## Date: October 6, 2019
## Class: EPSY 5200

## Exercise 33 from LP3TH by Zed Shaw

i = 0
numbers = []

while i < 6:
    print (f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print (f"Numbers now: ", numbers)
    print (f"At the bottom i is {i}")

print ("The numbers: ")

for num in numbers:
    print (num)


def new_function (count):
    i = 0
    numbers = []

    while i < count:
        print (f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print (f"Numbers now: ", numbers)
        print (f"At the bottom i is {i}")

    print ("The numbers: ")

    for num in numbers:
        print (num)


print ("Call function")
print (new_function(7))

## Study Drills
# 1) Converted as requested. Function is called 'new_function'
# 2) I have tried different numbers.
# 3) I have added in the while statement that would allow a variance in the amount it could be increased by.
# 4) I re-wrote to automatically use the function.
# 5) Yes, the incrementor is still needed otherwise the loop will only occur once assuming a start varlue of 0.

## Mistakes
# 1) No mistakes in this script to my knowledge.