# file_io_04 Reading characters

with open("text_file.txt","r") as file:
    line = file.readline()
    line_2 = file.readline()
    
print(line)
print(line_2)