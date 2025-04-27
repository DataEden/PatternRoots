import sys # import sys module to get command line arguments
import os # import os module to check if the file exists
import regex # import regex module to use the regex_email function

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 3:
    raise ValueError("Please enter a valid input and output file name.")

# Get the input file name from command line arguments
fname = sys.argv[1] 

# Check if the input file exists
if not os.path.isfile(fname):
    raise ValueError("File does not exist.")

# Open the input file and read its contents
with open(fname, mode='r', encoding='utf8') as f:
    contacts = f.readlines()

# Check if the input file is empty
clist = []
for str in contacts:
    cstr = regex.regex_email(str)
    if 'email:' in cstr:
        clist.append(cstr + '\n')

# Check if the output file already exists 
# 
with open(sys.argv[2], mode='w', encoding='utf8') as f:
    f.writelines(clist)
    print(f"File {sys.argv[2]} created successfully.")