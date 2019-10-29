# UMN EPSY 5200: Programming Methods for Psychological Research
# Prof. Jeffrey K. Bye
# Assignment 8: Due Wednesday, October 30, 2019 by 2:30pm

# NAME: Robert Kreml

## Instructions
# For problems that require you to write code, write your code in the appropriate section below
# For problems that require you to provide a written response, write your answer as a comment (#)

# You should expect to make mistakes on this assignment. That is part of the learning process.
# Whenever you make a mistake, document the mistake AND what you learned from it in the section AT THE BOTTOM.

# As always, document any help you receive from online or friends.
# You must attempt each problem on your own first though! (Otherwise, you won't learn as well!)


#############
### PROBLEM 1

## 1a) Repeat the code from Week 8 class to load "Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx"
#       into Python as a Pandas data frame called 'act'

import pandas as pd
fname = 'Minnesota 2018 Public Schools Graduating Class 5 Year Trends.xlsx'
act = pd.read_excel(fname)

## 1b) Repeat the code from Week 8 class to subset the data to only those rows with
#        'School' as the 'Analysis Level'. Be sure you re-number the rows as well.
#      This subset of data should be called 'act_sch'

act_sch = act[act['Analysis Level'] == 'School']
act_sch = act_sch.reset_index(drop=True)

## 1c) Run the line of code below and comment on what you think it does.
#         Be sure to describe what term applies to ".mean()"
print(act_sch['Avg Math'].mean())

# This command takes the new subset of data that had the 'analysis level' as school and looks for the 'Avg Math' column.
# Then it takes the mean of that data. It then prints that number in terminal.


## 1d) Adapt the code above so that instead of printing the value,
#       it saves the value to a variable called 'avg_math'

avg_math = act_sch['Avg Math'].mean()

## 1e) Adapt the code from 1d so that you create a variable called 'avg_eng',
#       which is the mean value from the 'Avg Eng' column in act_sch.

avg_eng = act_sch['Avg Eng'].mean()

#############
### PROBLEM 2

## 2a) Adapt the code from Week 8 class where we generated a Boolean (True/False) Series
#       based on a logical comparison, e.g., act_sch.N > 50
#      For this comparison, the value should be True if that school's Avg Math value
#           is GREATER than the value in 'avg_math', and False otherwise

act_sch[avg_math > avg_eng]

## 2b) Adapt the code in 2a to create a new column in the act_sch data frame
#       called "AboveAvgMath", which is True if that Avg Math value is greater than avg_math
#      To do this, adapt the code from Week 8 class where we created the new column 'Blah'
#       BUT instead of writing a single value on the right-hand side of the assignment,
#       use your code from 2a that generates a whole Series of bools.
#      This problem may involve some trial and error, as we didn't cover this directly.
#       This is great practice for figuring solving novel problems in your future!


## 2c) Adapt the code from 2b to create a new column, "AboveAvgEng",
#       which is set to True if that Avg Eng value is greater than avg_eng.


## 2d) Use the sum() function, combined with logicals, to find:
#       The number of schools that are above average in math AND English
#       The number of schools that are above average in math BUT NOT English
#       The number of schools that are above average in English BUT NOT math
#       The number of schools that are *below* average in math AND English
#      NOTES: Remember that at the end of pandas_demo.py, we covered how to
#                  combine logicals into one statement.
#             Remember that sum() of bools returns the number of Trues.
#             The opposite of  ==  is  !=  ("not" equal)
#      This problem may involve some trial and error, as we didn't cover this directly.
#       This is great practice for figuring solving novel problems in your future!


## 2e) What do you notice about the numbers in 2d?  Write 1-2 sentences.


#############
### PROBLEM 3

## Describe a problem that is relevant to your research that you would like to work on for your final project.
#    Note that this project should take about 15-20 hours of work, but not much more or less than that.
#    The goal here is for you to practice applying what we learn in class to your own work.
#  A data-based project could involve scraping data from the internet (which we will cover), or importing your own data,
#    then processing that data, running statistics, plotting, etc.
#  A more program-based project could involve building a Python program that a user could interact with,
#    by providing text inputs that cause the program to do different things
#    (e.g., a more advanced version of our weather printer)
#  This problem is not a final draft of your project proposal -- it's just to get an idea of what might work.
#    I will speak with each student individually to help come up with a reasonable final project scope.
#  I expect approximately 4-6 sentences for this first draft of your project idea.


#############
### MISTAKE DOCUMENTATION
