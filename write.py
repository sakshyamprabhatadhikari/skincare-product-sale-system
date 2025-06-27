# write.py module is a 	Data Access + Reporting type module.
#write.py module is tesponsible for saving data to file and generating invoices.
#It bridges between business logic and persistent storage/output reporting.

#Importing datetime module to get current date and time
from datetime import datetime #from keyword is used to import only a specified section from a module.

# -------------------------- SAVE PRODUCTS --------------------------

def save_products(products, file_path="products.txt"):
    """
    Saves the updated product dictionary to the products.txt file.

    Args:
        products (dict): Dictionary of all products.
        file_path (str): File to which the product info is saved.
    """
    try:
        with open(file_path, "w") as file:
            # Convert each product's details to string and write to file
            for value in products.values():
                file.write(",".join([str(v) for v in value]) + "\n")
    except Exception as e:
        print("An error occurred while saving products:", e)


# -------------------------- GENERATE INVOICE --------------------------

def generate_invoice(transaction_type, customer_name, phone, items, total_amount):
    """
    Generates a transaction invoice (sale or purchase), writes it to a file,
    and displays it neatly in the Python IDLE.

    Args:
        transaction_type (str): Either 'sale' or 'purchase'.
        customer_name (str): Name of the customer or supplier.
        phone (str): Phone number of the customer or supplier.
        items (list): List of dictionaries containing product details.
        total_amount (float): Total bill amount.
    """
    now = datetime.now().strftime("%Y%m%d_%H%M%S")  # Timestamp for unique filename
    file_name = f"{transaction_type}_invoice_{customer_name.replace(' ', '_')}_{now}.txt"

    try:
        # ----------- HEADER & BASIC INFO -----------
        header = f"\n{'-'*80}\n"
        title = f"{'WeCare Wholesale - ' + transaction_type.title() + ' Invoice':^80}\n"
        date_info = f"Customer/Supplier: {customer_name}    Phone: {phone}    Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

        # ----------- COLUMN HEADERS -----------
        columns = f"\n{'Product':<20}{'Brand':<15}{'Qty':<8}{'Free':<8}{'Unit Price':<15}{'Total':<10}\n"
        divider = "-" * 80 + "\n"

        # ----------- ITEM LINES -----------
        item_lines = ""
        for item in items:
            # Each row aligned properly
            item_lines += f"{item['name']:<20}{item['brand']:<15}{item['qty']:<8}{item.get('free_qty', 0):<8}{item['unit_price']:<15.2f}{item['total']:<10.2f}\n"

        # ----------- TOTAL AND FOOTER -----------
        total_line = f"\n{'Total Payable Amount:':>65} Rs. {total_amount:.2f}\n"
        footer = "-" * 80 + "\n"

        # Combine all parts of the invoice
        full_invoice = header + title + header + date_info + columns + divider + item_lines + total_line + footer

        # Write the invoice to a text file
        with open(file_name, "w") as file:
            file.write(full_invoice)

        # Also display the invoice in Python IDLE
        print(full_invoice)

    except Exception as e:
        print("Error generating invoice:", e)
