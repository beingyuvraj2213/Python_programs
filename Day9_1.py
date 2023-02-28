# dictionary={"key":"value"}

programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily call over and over again",
    "Loop":"The action of doing something over and over again",
}

print(programming_dictionary["Function"])

# Adding new items in dictionary
programming_dictionary["Python"]="A high level programming language used for development"

print(programming_dictionary)

# Creating an empty dictionary
empty={}

# Edit an item in a dictionary
programming_dictionary["Bug"]="A moth in your computer"

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
