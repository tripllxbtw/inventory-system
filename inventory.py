products = {
    "milk": 6,
    "bread": 8,
    "eggs": 9,

}
# This program manages a simple inventory of products.
while True:
    choice = input("Please enter 'show', 'add', 'remove', 'update', or 'exit': ").strip().lower()
    if choice == "show":
        print(products)
    elif choice == "add":
        product_name = input("Enter the product name: ").strip().lower()
        product_quantity = int(input("Enter the product quantity: "))
        products[product_name] = product_quantity
    elif choice == "remove":
        products_rem = input("Enter the product name to remove: ").strip().lower()
        if products_rem in products:
            del products[products_rem]
            print(f"Product '{products_rem}' removed.")
        else:
            print(f"Product '{products_rem}' not found.")
    elif choice == "update":
        products_update = input("Enter the product name to update: ").strip().lower()
        if products_update in products:
            new_quantity = int(input(f"Enter the new quantity for '{products_update}': "))
            products[products_update] = new_quantity
            print(f"Product '{products_update}' updated to {new_quantity}.")
        else:
            print(f"Product '{products_update}' not found.")
    elif choice == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 'show', 'add', 'remove', 'update', or 'exit'.")
# End of inventory.py
# Save the updated products dictionary to a file
with open("products.txt", "w") as file:
    for product, quantity in products.items():
        file.write(f"{product}: {quantity}\n")
# Notify the user that the products have been saved
print("Products have been saved to products.txt")
# Notify the user that the program has ended
print("Program has ended.")
    