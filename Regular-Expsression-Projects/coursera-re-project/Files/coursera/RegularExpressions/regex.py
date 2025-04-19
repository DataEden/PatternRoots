
import re # Import the regular expression module

def regex_email(str): 
    """ 
    This function takes a string and returns True if it is a valid email address, otherwise False.
    A valid email address is defined as:
    
    Args:
        str (str): The input string to be checked.

    return: 

    """
    regex = r'^email:[a-z0-9_.-]+@[a-z0-9.-]+.{3}[a-z]$'
    pm = re.compile(r'email:')

    m = pm.match(str)
    if m:
        pm = re.compile(regex, re.IGNORECASE)
        m = pm.match(str)
        if m:
            return m.group()
        else:
            return 'invalid email'
    else:
        print("No email prefix found, searcching for email address...")
        # Check if the string matches the regex pattern for a valid email address
        p = re.compiler(r'^[a-z0-9_.-]+@[a-z0-9.-]+.{3}[a-z]$')
        m = p.match(str)
        if m:
            return 'email:' + m.group()  
        else:
             return 'invalid email' 
    """
    This function takes a string and returns True if it is a valid email address, otherwise False.
    A valid email address is defined as:
    - It starts with a letter (a-z, A-Z)
    - It contains an '@' symbol followed by a domain name (letters, numbers, hyphens, and dots are allowed)
    - The domain name must end with a top-level domain (TLD) of at least 2 characters (e.g., .com, .org, .net)
    """
   
       




