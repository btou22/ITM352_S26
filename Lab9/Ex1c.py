# Open the file names.txt and read its contents and print the number of names

file_object = open("names.txt")
contents = file_object.read()
contents_list = contents.split("\n")
print(contents)
print(f"Number of names: {len(contents_list)}") 
file_object.close()