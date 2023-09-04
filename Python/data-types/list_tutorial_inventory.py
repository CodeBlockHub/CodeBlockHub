# Initialize inventory
inventory = []

# Add Item
def add_item(item):
    inventory.append(item)
    print(f"Added {item} to the inventory.")

# Remove Item
def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"Removed {item} from the inventory.")
    else:
        print(f"{item} is not in the inventory.")

# List All Items
def list_items():
    print("Items in the inventory:")
    for item in inventory:
        print(item)

# Check Item Availability
def check_availability(item):
    if item in inventory:
        print(f"{item} is available.")
    else:
        print(f"{item} is not available.")

# Using the Functions
add_item("Apple")
add_item("Banana")
list_items()
check_availability("Apple")
remove_item("Apple")
list_items()