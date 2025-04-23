'''
Pseudocode:
# inventory.py - Clothing Store Inventory Tracking System

# Step 2: Creating the Inventory Dictionary
inventory = {}

# Step 3: Adding Items
def add_item(item_id, name, quantity):
    """
    Add a new item to the inventory.
    
    Parameters:
        item_id (str): Unique identifier for the item
        name (str): Name of the item
        quantity (int): Current quantity in stock
    """
    item_details = {"name": name, "quantity": quantity}
    inventory[item_id] = item_details
    print(f"Added {name} (ID: {item_id}) with quantity {quantity} to inventory.")

# Step 4: Checking Stock
def check_stock(item_id):
    """
    Check the current stock of an item.
    
    Parameters:
        item_id (str): Unique identifier for the item
    """
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    else:
        print(f"Item with ID {item_id} not found in inventory.")

# Step 5: Updating Stock
def update_stock(item_id, delta):
    """
    Update the stock quantity of an item.
    
    Parameters:
        item_id (str): Unique identifier for the item
        delta (int): Amount to change the quantity (positive for adding, negative for removing)
    """
    if item_id in inventory:
        inventory[item_id]["quantity"] += delta
        print(f"Stock for item {item_id} updated. New quantity: {inventory[item_id]['quantity']}")
    else:
        print(f"Item with ID {item_id} not found in inventory. Update failed.")

# Test the functions with sample data
if __name__ == "__main__":
    # Add some sample items
    add_item("TS001", "Blue T-Shirt", 25)
    add_item("TS002", "Red T-Shirt", 15)
    add_item("JN001", "Black Jeans", 10)
    add_item("JN002", "Blue Jeans", 12)
    add_item("SW001", "Hoodie Sweatshirt", 8)
    
    # Display all inventory items
    print("\nCurrent Inventory:")
    for item_id, details in inventory.items():
        print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}")
    
    # Check stock of specific items
    print("\nChecking Stock:")
    check_stock("TS001")
    check_stock("JN001")
    check_stock("SW002")  # Non-existent item
    
    # Update stock
    print("\nUpdating Stock:")
    update_stock("TS001", 5)    # Add 5 Blue T-Shirts
    update_stock("JN001", -3)   # Remove 3 Black Jeans
    update_stock("SW002", 10)   # Try to update non-existent item
    
    # Check stock after updates
    print("\nInventory After Updates:")
    check_stock("TS001")
    check_stock("JN001")
'''

inventory = {}

def add_item(item_id, name, quantity):
    item_details = {"name": name, "quantity": quantity}
    inventory[item_id] = item_details
    print(f"Added {name} (ID: {item_id}) with quantity {quantity} to inventory.")

def check_stock(item_id):
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    else:
        print(f"Item with ID {item_id} not found in inventory.")

def update_stock(item_id, delta):
    if item_id in inventory:
        inventory[item_id]["quantity"] += delta
        print(f"Stock for item {item_id} updated. New quantity: {inventory[item_id]['quantity']}")
    else:
        print(f"Item with ID {item_id} not found in inventory. Update failed.")

if __name__ == "__main__":
    add_item("TS001", "Blue T-Shirt", 25)
    add_item("TS002", "Red T-Shirt", 15)
    add_item("JN001", "Black Jeans", 10)
    add_item("JN002", "Blue Jeans", 12)
    add_item("SW001", "Hoodie Sweatshirt", 8)

    print("\nCurrent Inventory:")
    for item_id, details in inventory.items():
        print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}")
    
    print("\nChecking Stock:")
    check_stock("TS001")
    check_stock("JN001")
    check_stock("SW002")  

    print("\nUpdating Stock:")
    update_stock("TS001", 5)    
    update_stock("JN001", -3)   
    update_stock("SW002", 10)   
    
    print("\nInventory After Updates:")
    check_stock("TS001")
    check_stock("JN001")