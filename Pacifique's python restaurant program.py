class Pacifique:
    def __init__(self):
        # Define the menu with the price of each item of the restaurant
        self.menu = {
            "coffee": 2000,
            "black tea": 1500,
            "green tea": 2000,
            "burundian milk": 1800,
            "buffet": 6000,
            "chicken": 35000,
            "fish": 12000,
            "breakfast": 10000,
            "agatoki": 1200,
            "akabenzi": 15000,
            "cappucino coffe": 5000,
            "Roasted Chicken": 25000,
            "1/2 of a Chicken": 15000,
            "Spaghetti":8000,
            "Omolette": 4800,
            "Shawarma": 6500,
            "Rolex": 4800,
            "Special Rolex":9000,
            "humberger": 15000,
            "Sambusa":1500,
            "Capati": 500,
            "Umuceri": 3500,
            "brochette": 2500,
            "Brochette special": 9000,
            "salade": 4500,
            "salade special(macaroni)": 15000
        }

    def welcome_customer(self):
        # Greet the customer and ask for their name
        print("Welcome to Pacifique's restaurant!")
        while True:
            name = input("What's your name? \n ")
            # Check if name is a valid string
            if not name.isalpha():
                print("Invalid name! Please enter a valid name. \n")
                continue
            else:
                print(f"Hello {name}, we are happy  and excited to serve you today!!!")
                break

   

    def show_menu(self):
        # Display the menu with the price of each item
        print("Here's our menu:")
        for item, price in self.menu.items():
            print(f"{item.capitalize()}: {price} FBU")

    def calculate_price(self, order):
        # Calculate the total price of the order based on the menu and the quantity of each item
        total_price = 0
        for item, quantity in order.items():
            total_price += self.menu[item] * quantity
        return total_price

    def serve_customer(self):
        # Call the welcome_customer and show_menu methods to start the interaction with the customer
        self.welcome_customer()
        self.show_menu()
        order = {}
        while True:
            # Ask the customer what they would like to order and how many of each item they want
            item = input("What would you like to order? ")
            if item.lower() not in self.menu:
                # If the customer orders an item that is not on the menu, prompt them to choose again
                print("Sorry, we don't have that item in our menu. Please choose something from our menu.")
                continue
            quantity = int(input(f"How many {item}s would you like to have? "))
            order[item.lower()] = quantity
            more_items = input("Would you like to order more? (yes/no) ")
            if more_items.lower() == 'no':
                # If the customer is finished ordering, break out of the loop
                break
        total_price = self.calculate_price(order)
        # Display the total price and prompt the customer to wait while the order is prepared
        print(f"Great! Your total is {total_price} FBU.")
        print("Please wait a moment while we prepare your delicious Meal")
        print("...")
        # Display the customer's order
        print("Here's what you ordered: \n")
        for item, quantity in order.items():
            print(f"{quantity} {item.capitalize()}({self.menu[item] * quantity} FBU)")
        print("Enjoy your meal!")
        # Ask the customer if they would like to order more, and return True if they do, False if they don't
        return input("Would you like to order more? (y/n) ").lower() == 'y'

    def start(self):
        # Call the serve_customer method until the customer is finished ordering
        while True:
            wants_to_order = self.serve_customer()
            if not wants_to_order:
                # If the customer is finished ordering, say goodbye and terminate the program
                print("Thank you for visiting Pacifique's restaurant. We hope to see you again soon!")
                break


if __name__ == '__main__':
    # Create an instance of the Pacifique class and call the start method to begin the program
    pacifique = Pacifique()
    pacifique.start()
