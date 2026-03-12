# Open the file names.txt and read its contents and print the number of names

file_object = open("names.txt")
contents_list = file_object.readlines()
print(contents_list)
print(f"Number of names: {len(contents_list)}") 
file_object.close()