#Create a list of tuples that are percentiles of household income
import numpy as np

hh_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]

hh_income_array = np.array(hh_income)

#Report the dimensions of the array, and the number of elements in the array.
print("Dimensions of the array: ", hh_income_array.ndim)
print("Dimensions v2: ", hh_income_array.shape)
print("Number of elements in the array: ", hh_income_array.size) 
    #Counts the product of the dimensions (2 x 9 = 18)


for i in range(len(hh_income_array)):
    print(i, hh_income_array[i][0], hh_income_array[i][1])
        # Prints the index, first element of the tuple (percentile), and second element of the 
        # tuple (income) for each tuple in the array.