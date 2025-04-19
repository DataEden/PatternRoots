
import re

def regex_email(str):
    pm = re.compile(r'email:')
    m = pm.match(str)

    return m.group() 
    """
    This function takes a string and returns True if it is a valid email address, otherwise False.
    A valid email address is defined as:
    - It starts with a letter (a-z, A-Z)
    - It contains an '@' symbol followed by a domain name (letters, numbers, hyphens, and dots are allowed)
    - The domain name must end with a top-level domain (TLD) of at least 2 characters (e.g., .com, .org, .net)
    """
   
       




