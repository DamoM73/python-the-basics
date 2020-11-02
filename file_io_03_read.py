# file_io_03 Read

with open("text_file.txt","r") as file:
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    
    text = file.read()
    
print(text)