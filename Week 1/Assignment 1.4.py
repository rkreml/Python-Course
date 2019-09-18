## Name: Robert Kreml
## Date: September 6, 2019
## Class: EPSY 5200

## Exercise 4 from LP3TH by Zed Shaw

cars = 100 # Number of cars.
space_in_a_car = 4.0 # Number of seats available in the cars.
drivers = 30 # Number of drivers to carpool with.
passengers = 90 # Number of passengers in the carpool.
cars_not_driven = cars - drivers # This is taking the number of drivers and subtracting the number of drivers to show how many cars will not be used.
cars_driven = drivers # This is just setting that the number of drivers will also equal the amount of cars being driven.
carpool_capacity = cars_driven * space_in_a_car # This is the overall amount of carpool space possible.
average_passengers_per_car = passengers / cars_driven # This is trying to calculate how many passengers need to be in each car on average to get all of the passengers to their destinations.


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

## Study Drills
# 0) The error being described in the first study drill is because they did not actually create a variable called "car_pool_capacity" before that recall line of code. So python could not recall something that did not exist.
# 1) It really depends on the variable. In this case I could see it being justified if there was a half seat somewhere in the vehicle. If a fraction of an integer makes sense for the variable it is necessary. If just 4 was used, the floating pointer would not show up therefore
# line 20 would print out 120 not 120.0 and line 22 would print out 3 not 3.0 because there is no floating pointer being used.
# 2) I remembered.
# 3) I added comments explaining what each of the variables does.
# 4) I know that = means equals and it is defining data and assigning it to a variable for python to retrieve later in the script in this case.
# 5) I also remember that underscore characters are a thing.
# 6) I will reuse my old "Assignment 1.3.b.py" and create a new script "Assignment 1.4.b.py" where I change some of the equations into variables and use them for quicker calculations.

## Mistakes
# 1) None were made in this script.