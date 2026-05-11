class ShoppingCart: 
    def __init__(self, cust_name=None, cust_date=None):
        if cust_date:
            self.cust_date = cust_date
        else:
            self.cust_date = "January 1, 2020"
        if cust_name:
            self.cust_name = cust_name
        else:
                self.cust_name = "none"
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print(f'Description: {ItemToPurchase.name}')
        print(f'Price: {ItemToPurchase.price}')
        print(f'Quantity: {ItemToPurchase.quantity}')

    def remove_item(self, itemname):
        self.cart_items.remove(itemname)

    def modify_item(self, ItemToPurchase, new_description=None, new_price=None, new_quantity=None):
        if ItemToPurchase in self.cart_items:
            if ItemToPurchase.name != None:
                ItemToPurchase.name = new_description
            if ItemToPurchase.price != 0:
                ItemToPurchase.price = new_price
            if ItemToPurchase.quantity != 1:
                ItemToPurchase.quantity = new_quantity
            print(("Desc", ItemToPurchase.name),("Price", ItemToPurchase.price),("Qty", ItemToPurchase.quantity))

    def get_num_items_in_cart(self):
        total_items = 0
        for i in self.cart_items:

           total_items += i.quantity
        return total_items
    def get_cost_of_cart(self):
        total_price = 0
        for i in self.cart_items: 
            total_price += i.price * i.quantity
        return total_price
    
    def print_total(self):
        """
        Outputs total of objects in cart.
        If cart is empty, output this message: SHOPPING CART IS EMPTY
        print_descriptions()
        Outputs each item's name.
        Example of print_total() output:
        John Doe's Shopping Cart - February 1, 2020
        Number of Items: 8
        Nike Romaleos 2 @ $189 = $378
        Chocolate Chips 5 @ $3 = $15
        Powerbeats 2 Headphones 1 @ $128 = $128
        Total: $521
        """
   
        if not self.cart_items: 
            print ("Shopping cart is empty\n".upper())
        else:
            print(f"{self.cust_name}'s Shopping Cart - {self.cust_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            
            for i in self.cart_items:
                print("Item Descriptions")
                print(f"{i.name} {i.quantity} @ ${i.price} = ${i.quantity * i.price}")
            
            print("Total: ", self.get_cost_of_cart())
    
    def print_descriptions(self):
        """
        Example of print_descriptions() output:
        John Doe's Shopping Cart - February 1, 2020
        Item Descriptions
        Nike Romaleos: Volt color, Weightlifting shoes
        Chocolate Chips: Semi-sweet
        Powerbeats 2 Headphones: Bluetooth headphones
        """
        print(f"{self.cust_name}'s Shopping Cart - {self.cust_date}")
        print("Item Descriptions")
        for i in self.cart_items:
            print(f"{i.name}: {i.description}")

class Item:
    def __init__(self, name=None, price=0, quantity = 1, description = None):
        self.name = name
        self.price = float(price)
        self.quantity = float(quantity)
        self.description = description
        



name_input = input("Enter customer's name: ")
date_input = input("Enter today's date: ")
shoppingcart = ShoppingCart(name_input, date_input)
print(f"Customer name: {name_input}")
print(f"Today's date: {date_input}")
while True: # keep menu running 
    while True: # keep valid character check running 
        inp = input("Choose an option: ")
        if inp in "arcioq":
            break
    if inp == "q": 
        break
    elif inp == "a":
        item_name = input("What is your item called? ")
        item_price = float(input("How much does it cost? "))
        item_qty = int(input("How many of them are in the cart? "))
        item_desc = input("What is its description? ")

        new_item = Item(name=item_name, price=item_price, quantity=item_qty, description=item_desc)
        shoppingcart.add_item(new_item)

    elif inp == "r":
        removed_item = input("What item do you want to remove? ")
        for elem in shoppingcart.cart_items:
            if elem.name.lower() == removed_item.lower():
                shoppingcart.remove_item(elem)
        
    elif inp == "c":
        new_qty = int(input("What is the new quantity? "))
        adjusted_item = input("What item do you want to change the quantity of? ")
        for idx, elem in enumerate(shoppingcart.cart_items):
            if elem.name == adjusted_item:
                shoppingcart.cart_items[idx].quantity = new_qty
    elif inp == "i":
        shoppingcart.print_descriptions()
    elif inp == "o":
        shoppingcart.print_total()


