# file_io_10 append file

with open("new_text_file.txt","a") as file:
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    
    file.write("Hello World!")
