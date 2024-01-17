'''Provide suitable variable names for the information to be inputted by the user.
Using the input function provide strings that ask user to enter
information.
'''

name = input("Enter your name:")
surname = input("Enter your surname:")

# As the full name needs to appear in the printed sentence,
# concatenation of name and surname with an empty string
# inbetween the name and surname will be necessary.
full_name = name + ' ' + surname

age = input("Enter your age:")
house_number = input("Enter your house number:")
street_name = input("street name:")


'''The information gathered now needs to be printed as a sentence so
the print function will need to be used with concatenation of the
variables arranged appropriately with the addition of empty strings
for spaces between words. End the sentence with the fullstop.
'''

print(full_name + ' ' + "is" + ' ' + age + ' ' + "years old and lives at" ' ' 
      + house_number + ' ' + street_name + ".")



