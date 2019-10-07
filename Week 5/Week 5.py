## Create a new function that ONLY converts ages
# Inputs: num: a single number
#   inUnits: "y", "m"
#   outUnits: "y", "m"

def age_converter(number, in_unit, out_unit):
    if in_unit is "y":
        if out_unit is "y":
            return(print(f"The participant's age is {number} years old."))
        elif out_unit is "m":
            number = number * 12
            return(print(f"The participant's age is {number} months old."))
        else:
            raise ValueError("Output unit must be 'y' or 'm'.")
    elif in_unit is "m":
        if out_unit is "y":
            number = number / 12
            return(print(f"The participant's age is {number} years old."))
        elif out_unit is "m":
            return(print(f"The participant's age is {number} months old."))
        else:
            raise ValueError("Output unit must be 'y' or 'm'.")
    else:
        raise ValueError("Input unit must be 'y' or 'm'.")

age_converter(56, "m", "y")