# Calculate average, minimum and maximum for the "ITProjectManagement.csv" file
import csv

file_name = "ITProjectManagement.csv"

with open(file_name) as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)  # Skip the header row

    total_cost = 0.0
    min_cost = 0
    max_cost = 0
    num_projects = 0

    for line in csv_reader:
        project_salary = float(line[2])  # salary is in the third column
        total_cost += project_salary
        if project_salary < min_cost or min_cost == 0:
            min_cost = project_salary
        if project_salary > max_cost:
            max_cost = project_salary
        num_projects += 1

    average_cost = total_cost / num_projects

    print(f"Total cost: ${total_cost:.2f}")
    print(f"Average cost: ${average_cost:.2f}")
    print(f"Minimum cost: ${min_cost:.2f}")
    print(f"Maximum cost: ${max_cost:.2f}")