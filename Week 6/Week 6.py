## Challenge in class:
# Define a list of 10 numbers (age in months)

# Print out:
# The mean age in years is X.
# There were Y total ages.

def mean(nums):
    # here, let's calculate the mean
    sum_nums = 0
    n_nums = 0
    while nums: # While there are numbers still in the list, so basically the length of the list no matter what.
        current_num = nums.pop()
        sum_nums = sum_nums + current_num
        n_nums = n_nums + 1 # n_nums += 1 can also be used.
    mean_nums = sum_nums / n_nums # then compute arithmetic mean
    return(mean_nums) # return

def age_mean(ages):
    # first we need to convert the months into years
    # initialize an empty list for converted ages to be saved into.
    converted_ages = []
    while ages:
        age = ages.pop()
        converted_age = age / 12
        converted_ages.append(converted_age)
    # next we are initializing the variables for the function
    sum_ages = 0
    n_ages = 0
    while converted_ages: # looks at our new list of converted ages.
        current_ages = converted_ages.pop()
        sum_ages = sum_ages + current_ages
        n_ages += 1
    mean_ages = round(sum_ages / n_ages, ndigits = 3)
    print(f"The mean age in years is {mean_ages}.")
    print(f"There were {n_ages} total ages.")

