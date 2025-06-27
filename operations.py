# operations.py module is a Business Logic Module
#operations.py contains core application logic (e.g., selling and restocking). It processes data and defines how the application behaves.

from write import generate_invoice, save_products #from keyword is used to import only a specified section from a module.

# -------------------------- DISPLAY PRODUCTS --------------------------

def display_products(products): #display_products function is created here.
    """
    Display the list of all products in a formatted table.
    """
    print("\nHere are the available products below:")
    print("ID\tName\t\tBrand\t\tStock\tPrice (Rs.)\tOrigin")
    print("-" * 80)
    
    # Loop through product dictionary and display each product
    for pid, (name, brand, qty, cost, origin) in products.items():
        print(f"{pid}\t{name:<10}\t{brand:<10}\t{qty}\t{cost * 2:.2f}\t\t{origin}")
    print("-" * 80)


# -------------------------- SELL PRODUCT --------------------------

def sell_product(products):
    """
    Handle the selling process including cart, free offer, and invoice generation.
    """
    customer_name = input("\nEnter the customer's name: ")
    phone = input("Enter the customer's phone: ")
    
    cart = []   # List to hold sold items
    total = 0   # Total sale amount

    while True:
        display_products(products)  # Show available products

        try:
            # Ask for product ID
            product_id = int(input("Enter the product ID you want to sell: "))
            if product_id <= 0:
                print("Invalid product ID. The product ID cannot be negative or zero. Please try again.")
                continue
            if product_id not in products:
                print("Invalid product ID. The product ID cannot be non-existed value. Please try again.")
                continue

            # Ask for quantity to sell
            qty = int(input("Enter the quantity you want to sell: "))
            if qty <= 0:
                print("Invalid quantity. The amount of quantity cannot be negative or zero. Please try again.")
                continue 
            
            name, brand, stock, cost_price, origin = products[product_id]

            # Apply "Buy 3 Get 1 Free" offer
            free_qty = qty // 3
            total_qty = qty + free_qty

            # Check for stock availability
            if total_qty > stock:
                print("There is not enough stock. Please enter a smaller quantity.")
                continue

            # Deduct total (including free) quantity from stock
            products[product_id][2] -= total_qty

            # Set unit price to double the cost price
            unit_price = cost_price * 2
            item_total = qty * unit_price  # Only paid quantity counts in total

            # Display offer message if applicable
            if free_qty > 0:
                print(f"\n Congratulations! You have qualified for our 'Buy 3 Get 1 Free' offer and have received {free_qty} item(s) free!")

            print("Thank you for buying from WeCare Wholesale!\n")

            # Add item to cart
            cart.append({
                "name": name,
                "brand": brand,
                "qty": qty,
                "free_qty": free_qty,
                "unit_price": unit_price,
                "total": item_total
            })

            total += item_total  # Update total sale amount

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Ask user if they want to sell another product
        more = input("Do you want to sell another product? (y/n): ").lower()
        if more != 'y':
            break

    # Finalize sale: generate invoice and save product changes
    generate_invoice("sale", customer_name, phone, cart, total)
    save_products(products)
    print("Sale completed. Invoice has been generated and saved.\n")


# -------------------------- RESTOCK PRODUCT --------------------------

def restock_product(products):
    """
    Handle the restocking of existing products and update inventory.
    """
    supplier_name = input("\nEnter the supplier's name: ")
    phone = input("Enter the supplier's phone: ")

    cart = []  # List to hold restocked items
    total = 0  # Total purchase cost

    while True:
        display_products(products)

        try:
            # Ask for product ID to restock
            product_id = int(input("Enter the product ID you want to restock: "))
            if product_id <= 0:
                print("Invalid product ID. The product ID cannot be negative or zero. Please try again.")
                continue
            if product_id not in products:
                print("Invalid product ID. The product ID cannot be non-existed value. Please try again.")
                continue

            # Ask for quantity
            qty = int(input("Enter the number of quantity you want to restock: "))
            if qty <= 0:
                print("Invalid quantity. The amount of quantity cannot be negative or zero. Please try again.")
                continue

            # Add quantity to existing product stock
            products[product_id][2] += qty #products dictionary is accessed and updated during restocking
            name, brand, _, cost_price, _ = products[product_id]

            # Calculate total cost for the product
            item_total = qty * cost_price

            # Add item details to cart
            cart.append({
                "name": name,
                "brand": brand,
                "qty": qty,
                "unit_price": cost_price,
                "total": item_total
            })

            total += item_total  # Update total cost
            print("Thank you for restocking this product! Inventory has been updated.\n")

        except ValueError:
            print("Invalid input. Please enter valid values.")
            continue

        # Ask if the user wants to restock more items
        more = input("Do you want to restock another product? (y/n): ").lower()
        if more != 'y':
            break

    # Generate invoice and save updated products
    generate_invoice("purchase", supplier_name, phone, cart, total)
    save_products(products)
    print("Restocking completed. Invoice has been generated and saved.\n")
