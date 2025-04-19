import sys
import os
import regex

if len(sys.argv) != 3:
    raise ValueError("Please enter a valid input and output file name.")

fname = sys.argv[1]

if not os.path.isfile(fname):
    raise ValueError("File does not exist.")

with open(fname, mode='r', encoding='utf8') as f:
    contacts = f.readlines()

for str in contacts:
    cstr = regex.regex_email(str)





