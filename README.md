# lab-inventory-tracking
Foundations I - Lab: Inventory Tracking

Lab: Inventory Tracking
For this lab, imagine you're a junior software engineer working for a clothing store. The store needs a program to track their inventory. Currently, they have a list of items, but it's difficult to quickly access information about specific items (size, quantity, etc.). Dictionaries are a helpful solution for this scenario.

In this lab, you will create a Python program that uses a dictionary to store information about each item in the inventory. This will allow the organization to easily access and update item details.

Tools and Resources
Review the dictionary content in the module, and code through the steps of the technical lesson and practice. 
Code this lab using the Python IDE, Visual Studio Code.
Instructions
Step 1: Setting Up
Create a new Python file named inventory.py 

Step 2: Creating the Inventory Dictionary
Define a dictionary named inventory to store item information. Each key will be a unique item identifier (e.g., a product code), and the value will be another dictionary containing details about that item.

Code: inventory = {}

Step 3: Adding Items
Create a function called add_item that takes three arguments:

item_id: The unique identifier for the item (string)
name: The name of the item (string)
quantity: The current quantity in stock (integer)
Inside the function:

Create a new dictionary to store the item's details with keys name and quantity.
Add the new dictionary with the item_id as the key to the main inventory dictionary.
Call the add_item function to add a few sample items to your inventory (e.g., T-shirts, jeans, etc.).
def add_item(item_id, name, quantity):
    item_details = {"name": name, "quantity": quantity}
    inventory[item_id] = item_details
Step 4: Checking Stock
Create a function called check_stock that takes an item_id as input. 

Inside the function:

Use a conditional statement to check if the item_id exists in the inventory dictionary.
If it exists, print the item's name and quantity from the nested dictionary.
If it doesn't exist, print a message indicating the item is not found.
Call the check_stock function to test it with existing and non-existent item IDs.
def check_stock(item_id):
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    else:
        print(f"Item with ID {item_id} not found in inventory.")
Step 5: Updating Stock
Create a function called update_stock that takes three arguments:

item_id: The unique identifier for the item (string)
delta: The amount to change the quantity (integer, positive for adding, negative for removing)
Inside the function: Check if the item_id exists in the inventory dictionary.

If it exists:
Access the item's current quantity.
Update the quantity by adding the delta value.
Update the nested dictionary within inventory with the new quantity.
If the item doesn't exist, print a message indicating the update failed.
Call the update_stock function to increase or decrease the stock quantity for specific items.

def update_stock(item_id, delta):
    if item_id in inventory:
        inventory[item_id]["quantity"] += delta
        print(f"Stock for item {item_id} updated.")
    else:
        print(f"Item with ID {item_id} not found in inventory. Update failed.")
Submission
Click the Load Lab: Inventory Tracking button to launch your Codegrade assignment. 
Upload your Python file (inventory.py) to the click here or add files to upload field. 
For additional information on submitting assignments in CodeGrade: Getting Started in CanvasLinks to an external site..
Grading Criteria
Use the rubric below as a guide for how this lab is graded.
You submission will be automatically scored in CodeGrade.
You can review your submission in CodeGrade and see your final score in your Canvas grades.
Lab: Inventory Tracking
Criteria
Function- Add Item

Excelled

No Attempt
Function- Check Stock

Excelled

No Attempt
Function- Update Stock

Excelled

No Attempt
