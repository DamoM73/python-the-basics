# file_io_04 Reading characters

with open("text_file.txt","r") as file:
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    
    chars = file.read(11)
    
print(chars)