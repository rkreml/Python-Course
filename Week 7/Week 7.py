fname = "Minn_ACT_Scores.csv"
# open_file = open(fname)
# print(type(open_file))

# act0 = open_file.read()
# print(type(act0))
# print(act0)

import csv
with open(fname, 'r', encoding ='utf-8-sig') as f:
    act1 = list(csv.reader(f))
math_ind = act1[0].index('Avg Math')
print(float(act1[1][math_ind]) * 2)

for r in range(1, len(act1)):
    print(act1[r][math_ind])

print(float(r[math_ind] for r in act1[1:]))

import numpy as np
act2 = np.genfromtxt(fname, delimiter=",", skip_header=1)
act2_vars = np.genfromtxt(fname, delimiter=",", max_rows=1, dtype="str", encoding="utf-8-sig")
print(act2_vars)
print(act2)
