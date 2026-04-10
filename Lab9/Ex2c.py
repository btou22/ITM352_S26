# use pathlib to open the file only if it exists and is readable and 
# print out some file information such as size.


from pathlib import Path
file_path = Path("ITProjectManagement.csv")

if file_path.is_file() and file_path.stat().st_size > 0:
    print(f"File '{file_path.name}' exists and is readable.")
    print(f"File size: {file_path.stat().st_size} bytes")
else:
    print(f"File '{file_path.name}' does not exist or is not readable.")