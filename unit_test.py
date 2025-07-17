# unit_test.py
import pytest
from inventory_service import add_item, get_inventory_count

def test_add_item_new():
    inventory = {}
    result = add_item(inventory, "laptop", 5)
    assert result["laptop"] == 5

def test_add_item_existing():
    inventory = {"mouse": 3}
    result = add_item(inventory, "mouse", 2)
    assert result["mouse"] == 5

def test_get_inventory_count_exists():
    inventory = {"keyboard": 10}
    assert get_inventory_count(inventory, "keyboard") == 10

def test_get_inventory_count_not_exists():
    inventory = {}
    assert get_inventory_count(inventory, "monitor") == 0