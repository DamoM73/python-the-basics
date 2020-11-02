# file_io_09 writing files

with open("new_text_file.txt","w") as file:
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    
    file.write("Hello World!")
