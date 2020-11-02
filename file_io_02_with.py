# file_io_02 using with

with open("text_file.txt", "r") as file:
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    
    print(file.read())