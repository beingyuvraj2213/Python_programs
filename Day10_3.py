# Docstring

def format_name(f_name,l_name):
    """Take first and last name and format it
    to return the title case version of the name"""

    if f_name=="" and l_name=="":
        return "You didn't provide valid inputs."

    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    new_name=formated_f_name+" "+formated_l_name
    return new_name

firstname=input("Enter your first name : ")
lastname=input("Enter your last name : ")

print(format_name(firstname,lastname))


