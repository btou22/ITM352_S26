# Read the 1,000 lines of taxi data from the taxi_1000.csv file
# Calculate the total of all fares, average fare, and the max
# trip distance.

import csv

filename = "taxi_1000.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)

    total_fare = 0.0
    max_distance = 0.0
    average_fare = 0.0
    num_rows = 0

    for line in csv_reader:
        if (num_rows == 0):  # Skip the header row and find the index of the fare and distance columns
            fare_index = line.index("Fare")
            distance_index = line.index("Trip Miles")
            num_rows += 1
            continue
        if (num_rows > 0):  # Skip the header row
            tripFare = float(line[fare_index])  # Fare is in the specified column
            tripDistance = float(line[distance_index])  # Trip distance is in the specified column
            total_fare += tripFare
            if tripDistance > max_distance:
                max_distance = tripDistance
        num_rows += 1

    if num_rows > 0:  # Ensure there are data rows to calculate average
        average_fare = total_fare / (num_rows - 1)  # Subtract 1 to exclude the header row

    print(f"We read {num_rows - 1} rows of data.")
    print(f"Total fare: ${total_fare:.2f}")
    print(f"Average fare: ${average_fare:.2f}")
    print(f"Max trip distance: {max_distance}")