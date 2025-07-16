# Imports exit() module function for the another_transaction() function
from sys import exit

# --- Product Menu ---
# product_menu() function relys on content in the dicitonary below
PRODUCT_PRICES = {
    # "PRODUCT-NAME": COST
    "BURGER": 3.25,
    "POP-DRINK": 1.75,
    "POUTINE": 4.50,
    "SALAD": 2.15,
    "FRENCH-FRIES": 0.75,
    "CHICKEN-STRIPS": 3.40,
    "CHICKEN-NUGGETS": 2.00,
    "MILKSHAKE": 2.50,
    "KIDS-MEAL": 1.50,
    "YUM-BISCUITS": 0.50,
    "FISH-SANDWICH": 2.00
}

def hor_line(): # Horizontal Line
    print('-'*70)

def product_menu(): 
        # Displays a Product Menu
        print("Product Menu:")
        hor_line() # Line Print
        # * Iterates through the dictionary by displaying 
        #   item names and prices
        for product, price in PRODUCT_PRICES.items():
            # * <22 aligns all product names on the left in a field
            #   that is 22 characters wide
            # * .2f displays all product prices with two decimal places
            # * Product Menu print changes when the product_price
            #   dictionary is changed
            print(f"{product:<30} - ${price:.2f}")
        hor_line() # Line Print

def option_interface():
    print("Welcome to the Fast Food Restaurant!")
    print("Made by Jayzee Monserate\n")
    print("-> Type 'A' to add a product.")
    print("-> Type 'Z' to view product prices.")
    print("-> Type 'X' to clear products.")
    print("-> Type 'V' to view your product list.")
    print("-> Type 'Q' to proceed to checkout.")

def entering_products():

    def clear_items():
        buying_data.clear()
        print("All items cleared!")

    def view_items():
        if len(buying_data) == 0:
            print("No items are in your order yet.")
            return # Prevents printing an empty table
        
        hor_line()
        print(f"{'Product':^30} | {'Quantity':^30} ")
        # * ^30 aligns all product names on the centre in a field
        #   that is 30 characters wide
        for product, quantity in buying_data.items():
            print(f"{product:^30} | {quantity:^30}")
        hor_line()

    buying_data = {} # Declares buying_data as a dictionary globally
    options = {
        # * Lambda is required for dictionary values with 
        #   passed arguments (i.e. buying_data below)

        "A": lambda: add_product(buying_data),
        "Z": product_menu,
        "X": clear_items,
        "V": view_items
    }

    product_entry = True
    
    while product_entry:
        option_input = input(
                "Type any option above (A/Z/X/V/Q) here: "
            # Strip and Upper functions reduces human error
            ).strip().upper()
        
        if option_input in options:
            options[option_input]()
        elif option_input == "Q":
            # Terminates the while product_entry loop
            product_entry = False
        else:
            print("Please type any of the letters specified above!")

    return buying_data

def add_product(buying_data):
    while True:
        try:
            product = input("Enter the product name: ").strip().upper()
            if product not in PRODUCT_PRICES: 
                # * Occurs if user inputs a product not in the 
                # PRODUCT_PRICES dictionary
                print(f"{product} is not in the menu!")
                continue
            quantity = int(input("Enter the quantity of the product: "))
            if quantity <= 0:
                print("Please enter a quantity greater than 0!")
                continue
            # Adds item to buying_data dictionary
            if product in buying_data:
                print(
                    f"{product} quantity will be changed from "
                    f"{buying_data[product]} to {quantity}."
                )

            buying_data.update({product: quantity})
            break
        # Raises exception if user inputs non-whole number
        except ValueError:
            print("Quantity input can only accept whole numbers!")

def price_dictionary(product, quantity):
    # [product] searches for the value with a given product name
    subtotal = PRODUCT_PRICES[product] * quantity
    print(
        f"{product}: ${PRODUCT_PRICES[product]:.2f} "
        f"x {quantity} = ${subtotal:.2f}"
    )
        
    return subtotal

def retrieve_discount(): 
    rewards_tiers = {
        "GOLD": 0.75, # 25% off on the customer's order
        "SILVER": 0.90, # 10% off on the customer's order
        "BRONZE": 0.95 # 5% off on the customer's order
    }

    discount = 0
    rewards_input = input(
        "Enter your rewards card tier (Gold/Silver/Bronze): "
    ).strip().upper()

    if rewards_input in rewards_tiers:
        discount = rewards_tiers[rewards_input]
        # .0f displays the discount rate with no decimal places
        print(f"Your discount rate is {((1 - discount) * 100):.0f}% "
            f"with a {rewards_input} rewards card.")
        return discount
    else:
        print("No discount for you!")
        return 1 # no discount on the customer's order

def receipt_print(buying_data, discount): 
    total_amount = 0 # Initializes total_amount as a float
    hor_line() # Line Print
    for key, value in buying_data.items():
        # Fetches products, their cost, and quantity from buying_data
        total_amount += price_dictionary(key, value)
    print(
        "\nThe total amount of your order " 
        f"{'is' if discount == 1 or total_amount < 15 else 'was'} " 
        f"${total_amount:.2f}."
        )

    # * Order must have a mininum total cost of $15 for a discount
    #   to be applied on checkout

    if discount < 1 and total_amount >= 15:
        discounted_amount = total_amount * discount
        print(
            f"\nHowever, with a {((1 - discount) * 100):.0f}% discount, "
            f"the total amount is now ${discounted_amount:.2f}."
        )

    # If user had a rewards card but spent less than $15 on their order       
    elif discount < 1 and total_amount < 15: 
        print(
            "\nYour order must amount to at least $15 " 
            "to be eligible for a discount."
            )
        
    else:
        print(
            "\nSign up for a rewards card today "
            "to receive a discount\n"
            "in any orders worth over $15!"
        )

    hor_line() # Line Print
    # .2f rounds the total amount to two decimal places

def another_transaction():
        print("-> Type 'Q' if you want to quit this program.")
        print(
                "-> Otherwise, type something else " 
                "to perform another order."
            )
        continue_option = input(
            "Type 'Q' or something else here: "
        ).strip().upper()

        if continue_option == "Q":
            print("END")
            exit() # Terminates the program from running
        else:
            return # Performs another transaction
        
        
if __name__ == "__main__":
    # * While loop is indefinite unless user types 'Q' in
    #   the another_transaction() function
    while True: 
        try:
            option_interface()
            buying_data = entering_products()
            discount = retrieve_discount()
            # * receipt_print() function passes the buying_data and discount  
            #   variables to calculate the costs of a customer's order
            receipt_print(buying_data, discount)
            another_transaction()

        # In case an exception occurs unexpectedly
        except Exception as e:
            print(e)
