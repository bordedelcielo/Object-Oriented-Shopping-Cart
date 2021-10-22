# Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

class convertStrings():
    def __init__(self):
        self.items = ""

    # Method to take string input
    def get_String(self):
        self.items = input('Please enter a message.')
    
    # Method to convert string to upper case only.
    def print_String(self):
        print(self.items.upper())

items = convertStrings()
items.get_String()
items.print_String()

# Rec from Ryan Rhoades:
# def showInventory(self):
#         if self.items == []:
#             print("Your bag is empty, gather some supplies quickly!")
#         else:
#             print("Here are your adventuring supplies!")
#             for item in self.items:
#                 print(item)

    
    # Method to 

# class IOString():
#     def __init__(self):
#         self.str1 = ""

#     def get_String(self):
#         self.str1 = input('Please enter a message and this program will convert lower case letters to upper case letters automatically.')

#     def print_String(self):
#         print(self.str1.upper())

# str1 = IOString()
# str1.get_String()
# str1.print_String()