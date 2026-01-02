# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

for item in inventory:
    print("Processing started")
    while inventory[item][0]<inventory[item][1]:
        print(f"Processing {item}")
        inventory[item][0] += inventory[item][2]
    if inventory[item][0] > discount_threshold and not inventory[item][3]:
        inventory[item][3] = True

    print("Processing completed")
        