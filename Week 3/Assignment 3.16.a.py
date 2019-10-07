## Name: Robert Kreml
## Date: September 23, 2019
## Class: EPSY 5200

## Exercise 16 Study Drill 2from LP3TH by Zed Shaw

from sys import argv
script, filename = argv
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
txt.close(filename)