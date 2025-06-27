# read.py module is a Data Access Module.

# ----------------------------------------------------------------------
# This module provides functionality to load product data from a file.
# It reads the products from 'products.txt' and stores them in a dictionary.
# Each product is assigned a unique product ID as the key.
# ----------------------------------------------------------------------

def load_products(file_path="products.txt"):
    """
    Loads product data from the specified text file and stores it in a dictionary.

    Parameters:
        file_path (str): The path to the file containing product data.
                         Defaults to "products.txt".

    Returns:
        dict: A dictionary where each key is a product ID (int),
              and the value is a list containing:
              [product name (str), brand (str), quantity (int),
               cost price (float), country of origin (str)].

    Error Handling:
        - If the file does not exist, prints an error and returns an empty dict.
        - If there is any other issue during reading or parsing, prints the error and returns an empty dict.
    """
    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            data = file.readlines()  # Read all lines from the file

        products = {}          # Dictionary to store product info
        product_id = 1         # Start product ID from 1

        # Loop through each line in the file
        for line in data:
            # Remove trailing newline and split values by comma
            name, brand, qty, cost_price, origin = line.strip().split(",")

            # Store the product data in dictionary with an integer key
            products[product_id] = [
                name,                     # Product name
                brand,                    # Brand
                int(qty),                 # Quantity in stock
                float(cost_price),        # Cost price as float
                origin                    # Country of origin
            ]

            # Increment product ID for next product
            product_id += 1

        return products

    # Handle missing file error
    except FileNotFoundError:
        print("Error: products.txt file not found.")
        return {}

    # Handle any other exception during file reading or parsing
    except Exception as e:
        print("An error occurred while loading products:", e)
        return {}
