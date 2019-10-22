# UMN EPSY 5200: Programming Methods for Psychological Research
# Prof. Jeffrey K. Bye
# Assignment 7: Due Wednesday, October 23, 2019 by 2:30pm

# NAME: Robert Kreml

## Instructions
# For problems that require you to write code, write your code in the appropriate section below
# For problems that require you to provide a written response, write your answer as a comment (#)

# You should expect to make mistakes on this assignment. That is part of the learning process.
# Whenever you make a mistake, document the mistake AND what you learned from it in the section AT THE BOTTOM.

# As always, document any help you receive from online or friends.
# You must attempt each problem on your own first though! (Otherwise, you won't learn as well!)

import numpy as np

#############
### PROBLEM 1

# Think about a type of small data set you might have in your research, with 2 IV and 1 DV.
#  One of the IVs should be a continuous variable (e.g., how many hours studied)
#   and the other IV should be a categorical variable (e.g., type of studying, condition, etc.)
#  The DV should be continuous.

## 1a. First, create a LIST of data for 10 participants' values for the CONTINUOUS IV.
#       The data can be completely fictional or real, but they must be FLOATS.
#       Save the list with a variable name that both describes *what* the variable is,
#         and also follows good naming style for readability.
#       In other words, I should be able to understand what the variable is from reading its name.
#       Also add a comment that fully describes what the IV represents.

hours_studied = float([1.0, 9.0, 12.5, 19.8, 26.7, 33.1, 2.8, 9.7, 10.8, 9.9])
# This IV is the number of hours studied as a float, which means the data is rounded to the nearest tenth of an hour.

## 1b. Next, create a LIST of data for 10 participants' values for the CATEGORICAL IV.
#       The data can be completely fictional or real, but they must be INTEGERS.
#       Save the list with a variable name that both describes *what* the variable is,
#         and also follows good naming style for readability.
#       The values of the IV should be INTEGERS that represent the different category levels.
#       Also be sure that these IV values are in the SAME ORDER as the IV values from 1a.
#       In other words, I should be able to understand what the variable & its levels are from reading.
#       Also add a comment that fully describes what the IV represents.
#           E.g., "0" is Control, "1" is Experimental, etc.

type_of_studying = int([1, 1, 1, 2, 0, 1, 1, 0, 1, 2])
# These are the types of studying that can be done. The numbers correspond into a cateogry type. 0 means the student used the study guide. 1 means the student went to the study session. And 2 means the student came to office hours.

## 1c. Now create a LIST of participants' 10 DV values (e.g., scores on an exam)
#       The data can be completely fictional or real.
#       Save the list according to the same rules as above.
#       Also be sure that the DV values are in the SAME ORDER as the IV values from 1a.
#       In other words, the 2nd # in the IV list should correspond to the 2nd # in the DV list.
#       Also add a comment that fully describes what the DV represents.

exam_scores = int([32, 55, 65, 79, 93, 99, 43, 57, 68, 71])
# These are the exam scores out of a possible 100 points.

## 1d. Now put all 3 variables, along with a participant ID/# list (1-10), into a single NUMPY ARRAY.
#       Remember that in class we built numpy arrays with np.array() and it built by ROW.
#       That is, each list we passed np.array() was a row in the 2-D array (matrix).
#       To build your numpy array by COLUMN instead, use np.column_stack() instead.
#       Here's a template:

subj_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = np.column_stack([subj_num, hours_studied, type_of_studying, exam_scores])

## 1e. Print out your numpy array. What do you notice about the data types?
#       What happened to your categorical IV? Subject number?  (Answer below as a comment.)

print(data)


#############
### PROBLEM 2

## 2a. Demonstrate two DIFFERENT ways to return the first 4 rows of data from your array.
#          By "different ways", I mean you must type anything differently (it can be similar in concept).

## 2b. Index your DV column of the data frame using its column index.

## 2c. Index your array to return just the DV for participant #4 only.
#       In other words, you'll be indexing both dimensions and should get ONE number back.

## 2d. Slice your numpy array so that you get all of the data for participant #5.

## 2e. Slice your numpy array so that you get BOTH IVs (but NO DVs) for participants #7-9.

## 2f. Slice your numpy array so that you get ONLY the categorical IV and the DV
#       and only for participants #3 and #6. (The result should be a 2x2 array.)


#############
### PROBLEM 3

## 3a. Use the np.mean() function to find the mean of the DV.
#       Save the DV mean as a variable with a meaningful and readable name, with a comment.


## 3b. Use the np.mean() function to find the mean of the continuous IV.
#       Save the continuous IV mean as a variable with a meaningful and readable name, with a comment.


#############
### PROBLEM 4

## 4a. Using any spreadsheet program (Excel, Numbers, Google Sheets, etc.),
#       create a spreadsheet with the same 4 column structure as above,
#       but create (fake or real) data for 20 participants.
#       Export the spreadsheet as a .csv (look up how if you don't know).
#       Attach your CSV file to your homework submission.
#       (no need to write anything here for this part)

## 4b. Adapt the code from class to use np.genfromtxt() to load in your CSV.

## 4c. Use the np.mean() function to find the mean of the DV from your CSV data.
#       Save the DV mean as a variable with a meaningful and readable name, with a comment.


## 4d. Use the np.mean() function to find the mean of the continuous IV from your CSV data.
#       Save the continuous IV mean as a variable with a meaningful and readable name, with a comment.



#############
### EXTRA CREDIT

## XCa. Using your Prob 4 data, replace the 2nd participant's DV score with the value np.NaN
#           (Remember that NaN stands for "Not a Number")
#           Note that np.NaN should be typed exactly as is (no quotes)
#           The assignment should be done in ONE line of code.
#           If you're not sure how to replace a value in a numpy array, look it up.

## XCb. Now use np.mean() on the DV column of data.
#         What do you get as a result?  Why?

## XCc. Now use np.nanmean() on the DV column of data.
#          What do you get as a result? Why?


#############
### MISTAKE DOCUMENTATION
