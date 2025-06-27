#A module in Python is simply a file containing Python code—functions, classes, variables, or runnable code—that can be imported and used in other Python programs.
##My project is implemented in a modular way and there are total of 4 custom modules named main.py, operations.py, read.py, write.py and 1 built-in module called datetime
#main.py module is a Controller / Entry Point type module
#main.py is the main driver of the program.
#It acts as the central hub, handling user interaction and routing control to appropriate functions.

# Import functions to read products and perform core operations
from read import load_products #from keyword is used to import only a specified section from a module.
from operations import sell_product, restock_product

# -------------------------- MAIN ENTRY POINT --------------------------

def main(): #main function is created here.
    """
    Main function that runs the WeCare Wholesale system.
    Displays a welcome message, loads product data,
    and provides a menu for selling or restocking products.
    """
    # Display company header
    print("\n" * 2)
    print("\t" * 6 + "WeCare Wholesale\n")
    print("\t" * 5 + "Sukedhara, Kathmandu | Phone No: 9756794241\n")
    print("-" * 150)
    print("\t" * 4 + "Welcome to the system, Admin! I hope you have a good day ahead!")
    print("-" * 150)

    # Load product data from file
    products = load_products()

    # If products couldn't be loaded (file missing, empty, or corrupted), exit the system
    if not products:
        return

    # Infinite loop to keep the menu active until user chooses to exit
    while True:
        # Show available options to the admin
        print("\nWhat would you like to do?\n")
        print("1. Sell a product to a customer")
        print("2. Restock a product from the supplier")
        print("3. Exit the system\n")
        
        try:
            # Get admin's choice
            choice = int(input("Enter your desired choice (1-3): "))

            # Option 1: Sell a product
            if choice == 1:
                sell_product(products)

            # Option 2: Restock products
            elif choice == 2:
                restock_product(products)

            # Option 3: Exit system
            elif choice == 3:
                print("\nThank you for using the system. Have a great day ahead!\n")
                break

            # If the entered number is not among the options
            else:
                print("Invalid option. Please choose 1, 2, or 3.\n")

        # If input is not a valid number
        except ValueError:
            print("Invalid input. Please enter a number (1-3).\n")


# Check if this script is running as the main program
# (and not being imported from another file)
if __name__ == "__main__":
    main()
