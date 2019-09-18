ages = [20, 22, 25, 19, 28, 54, 23, 12]
print(round(sum(ages) / len(ages), 2))

sum_ages = sum(ages)
n_ages = len(ages)
mean_ages = (sum_ages/n_ages)
max_ages = max(ages)
min_ages = min(ages)

print("The mean age of my sample of participants is:", round(mean_ages, 2), "years.")
print("The maximum age is:", max_ages, "years.")
print("The minimum age is:", min_ages, "years.")