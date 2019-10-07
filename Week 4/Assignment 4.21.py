## Name: Robert Kreml
## Date: October 1, 2019
## Class: EPSY 5200

## Exercise 21 from LP3TH by Zed Shaw

def add(a, b):
    print(f"ADDING {a} + {b}")
    return(a + b)

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 0.5)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

## Study Drills
# 1) I understand what the def function does and how to create my own functions.
# 2) The equation is: ((30 + 5) + (78 - 4) - (90 * 2) * ((100 / 2) / 2))
# 3) I changed the value of 'iq' to see what it did, and divided by 0.5 instead of 2. It changed the ultimate value of 'what' as expected and it changed the value of 'iq'.
# 4) The equation is: 34 + 12 - 12 + 37 / 2. The commands are below:

a = divide(37, 2)
b = add(34, 12)
c = subtract(a, 12)
d = add(c, a)
print(f"The answer is: {d}.")

## Mistakes
# 1) There were no mistakes in this script to my knowledge.