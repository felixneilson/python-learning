'''# ask user for their name
name = input("whats your name? ")

# remove whitespace from the beginning and end of the string
name = name.strip() 

#capitalize the first letter of the name
name = name.capitalize()

# capitalize the first letter of each word in the name
name = name.title()

#capitalise and remove whitespace from the beginning and end of the string
name = input("whats your name? ").strip().title()

#split user name into first and last name
first, last = name.split(" ")



# same thing but using f-string
print(f"hello, {first}")

'''

'''
# defining a function that takes a name as an argument and returns a greeting
def hello(person="world"):
    print(f"hello, {person}")

hello()
name = input("whats your name? ").strip().title()
hello(name)


'''
