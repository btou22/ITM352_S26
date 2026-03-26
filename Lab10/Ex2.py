# Create a dataframe from individual lists
# Do some simple statistics on the data

import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

#Create a dictionary from the list of ages and genders
dict = (zip(ages, gender))
#print(list(dict))

#Create a dataframe from the dictionary
df = pd.DataFrame(dict, index=names, columns=["Age", "Gender"])
    # index is called with names
print(df)

summary = df.describe()
print(summary)

#Calculate average age by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()
    # however many groups there are in gender, it will calculate the average age for each group
print("\nAverage age by gender: \n", average_age_by_gender)