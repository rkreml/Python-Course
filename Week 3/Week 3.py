# .format() version
resultOut = "47 / 3 is : {}"
print(resultOut.format(47/3))

# f-string version: formatted literal strings
result = 47/3
print(f"47 / 3 is: {result}")

month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

months = "Month {} is called {}."
m = 1
M = 'January'

print(months.format(m, M))