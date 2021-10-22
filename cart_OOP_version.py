class ShoppingCart():
    
    def __init__(self,items):
        self.items = items

    # Method to show inventory.
    def showShoppingCart(self):
        print("Your inventory contains the following items:")
        for item in self.items:
            print(item)

    # Method to return message if cart inventory is empty.
    def showEmptyCart(self):
        print("Your inventory is currently empty.")

    # Method to add items to the shopping cart.
    def addToShoppingCart(self):
        shopping_item = input("What would you like to add? ")
        self.items.append(shopping_item)

    # Method to remove items from the shopping cart.
    def removeFromShoppingCart(self):
        shopping_item = input("What would you like to remove?")
        self.items.remove(shopping_item)

# Creating an instance of the ShoppingBag Class
your_shopping_cart = ShoppingCart([])

# Create function to run the shoppingBag(wholeFoods_bag) methods

def run():
    while True:
        response = input('What do you want to do? add/show/remove/quit: ')

        if response.lower() == 'quit':
            your_shopping_cart.showShoppingCart()
            print('Thanks for shopping!')
            break
        elif response.lower() == 'add':
            your_shopping_cart.addToShoppingCart()
        elif response.lower() == 'remove':
            your_shopping_cart.removeFromShoppingCart()
        elif response.lower() == 'show':
            your_shopping_cart.showShoppingCart()

run()