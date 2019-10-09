# START WITH old functions:
def age_convert(num, inUnits = "y", outUnits = "m"):
    # these are NESTED if statements
    # remember our nested flowchart
    if inUnits is "y":
        if outUnits is "y":
            return(num) # if both are y, just return num
        elif outUnits is "m":
            return(num * 12) # if y to m, multiply by 12
        else: # otherwise, error for outUnits
            raise ValueError("outUnits must be 'y' or 'm'")
    elif inUnits is "m":
        if outUnits is "y": # if m to y, divide by 12
            return(num / 12)
        elif outUnits is "m": # if both m, just return num
            return(num)
        else: # otherwise, error for outUnits
            raise ValueError("outUnits must be 'y' or 'm'")
    else: # otherwise, error for inUnits
        raise ValueError("inUnits must be 'y' or 'm'")

# DEFINE a function called 'mean', that takes 1 argument:
#   nums: a list of numbers to find the mean of
# def mean(nums):
    # here, let's calculate the mean
    # sum_nums = sum(nums) # find the sum
    # n_nums = len(nums) # and the number (length) in list
    # mean_nums = sum_nums / n_nums # then compute arithmetic mean
    # return(mean_nums) # return

# In Class Practice:
# DEFINE a function called 'mean', that takes 1 argument:
#   nums: a list of numbers to find the mean of
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