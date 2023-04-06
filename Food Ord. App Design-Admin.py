import random
class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
def generate_food_id():
    return random.randint(1000, 9999)
menu = []
def add_food_item(name, quantity, price, discount, stock):
    food_id = generate_food_id()
    item = FoodItem(food_id, name, quantity, price, discount, stock)
    menu.append(item)
    return food_id
def edit_food_item(food_id, name=None, quantity=None, price=None, discount=None, stock=None):
    for item in menu:
        if item.food_id == food_id:
            if name is not None:
                item.name = name
            if quantity is not None:
                item.quantity = quantity
            if price is not None:
                item.price = price
            if discount is not None:
                item.discount = discount
            if stock is not None:
                item.stock = stock
            return True
    return False
def view_food_items():
    return menu
def remove_food_item(food_id):
    for item in menu:
        if item.food_id == food_id:
            menu.remove(item)
            return True
    return False
food_id = add_food_item("Pizza", "1 Large", 10.99, 0.2, 10)
print("Added food item with ID", food_id)
success = edit_food_item(food_id, "Pepperoni Pizza", "1 Large", 12.99, 0.3, 5)
if success:
    print("Edited food item with ID", food_id)
else:
    print("Could not find food item with ID", food_id)
all_food_items = view_food_items()
for food_item in all_food_items:
    print(food_item.food_id, food_item.name, food_item.quantity, food_item.price, food_item.discount, food_item.stock)
success = remove_food_item(food_id)
if success:
    print("Removed food item with ID", food_id)
else:
    print("Could not find food item with ID", food_id)

