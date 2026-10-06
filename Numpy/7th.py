import numpy as np 

# FILTERING

# Select elements from an array that match a given condition 

ages = np.array([[21,34,16,22,47,99,27],[55,50,19,16,18,26,22]])

teens = ages[ages < 18]

print(teens)

adults = ages[(18<ages) & (ages<40)]

print("ADULTS / " , adults)

seniors = ages[ages > 40]
print("Seniors", seniors)
