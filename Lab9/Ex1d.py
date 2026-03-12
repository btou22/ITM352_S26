# Open the file names.txt and read its contents and print the number of names

with open("names.txt") as file_object:
    while (line := file_object.readline()):
        print(line.strip())