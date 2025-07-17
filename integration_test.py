# integration_test.py
import pytest
from inventory_service import add_item, get_inventory_count

def test_full_flow():
    inventory = {}
    inventory = add_item(inventory, "tablet", 2)
    inventory = add_item(inventory, "tablet", 3)
    assert get_inventory_count(inventory, "tablet") == 5