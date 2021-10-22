#Write a function that prompts the user for their birth month and return there birthstone.
#If they input an invalid month tell them to try again
#Assume user inputs an integer number
stones={
    1:"Garnet",
    2:"Amethyst",
    3:"Aquamarine",
    4:"Diamond",
    5:"Emerald",
    6:"Pearl",
    7:"Ruby",
    8:"Peridot",
    9:"Sapphire",
    10:"Opal",
    11:"Topaz",
    12:"Turquoise"
}

# .isdigit()
# membership check
# given dictionary

def your_birthstone():
    while True:
        month = input("What month were you born in? Please enter your answer as an integer. Type 'quit' to quit: ")
        while not month.isdigit():
            month = input("Please enter an integer corresponding to a valid calendar month or type 'quit' to quit: ")
            while not int(month) < 13:
                month = input("Please enter an integer corresponding to a valid calendar month or type 'quit' to quit: ")
                birthstone = stones[int(month)]
                print(f'Your birthstone is {birthstone}.')

your_birthstone()

# FROM JOHN LOVELAND
# Here is a solution to the Whiteboard for today with error checking

# #Write a function that prompts the user for their birth month and return there birthstone.
# #If they input an invalid month tell them to try again
# #Assume user inputs an integer number
# stones={
#     1:"Garnet",
#     2:"Amethyst",
#     3:"Aquamarine",
#     4:"Diamond",
#     5:"Emerald",
#     6:"Pearl",
#     7:"Ruby",
#     8:"Peridot",
#     9:"Sapphire",
#     10:"Opal",
#     11:"Topaz",
#     12:"Turquoise"
# }

# def get_the_stones():
#     while True:  
#         month = input("Please enter your birth month or quit to exit: ")
#         while not month.isdigit() or not 0 < int(month) < 12:
#             month = input("Please enter a valid month or quit to exit: ")

#         if month == 'quit':
#             break
#         else:
#             print(f'Your birthston is {stones[int(month)]}')        

# get_the_stones()


# FROM  TERRELL
# def birthstones():
#     while True:
#         month = input("what is your integer birth month? type q to quit ")
#         if month == 'q':
#             break
#         months = [str(i) for i in range(1,13)]
#         if month in months:
#             print(f"Your birthstone is {stones[int(month)]}")
#         else: 
#             print('give us a valid month')
# birthstones()