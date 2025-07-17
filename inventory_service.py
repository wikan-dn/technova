# inventory_service.py
def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    return inventory


def get_inventory_count(inventory, item_name):
    return inventory.get(item_name, 0)