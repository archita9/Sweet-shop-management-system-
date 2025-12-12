
# Add project root to sys.path for import to work
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the SweetShop class from your package
from sweet import SweetShop
import pytest

# Test: Adding a sweet successfully

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet(1, "Ladoo", "Pastry", 10.0, 20)
    sweets = shop.view_sweets()
    assert len(sweets) == 1
    assert sweets[0]["name"] == "Ladoo"

# Test: Adding a sweet with missing fields
# Should raise ValueError

def test_add_missing_fields():
    shop = SweetShop()
    with pytest.raises(ValueError):
        shop.add_sweet(None, "", "Candy", None, None)

# Test: Deleting a sweet by ID

def test_delete_sweet():
    shop = SweetShop()
    shop.add_sweet(2, "Barfi", "Candy", 15.0, 5)
    shop.delete_sweet("Barfi")
    assert shop.view_sweets() == []

# Test: Searching for sweet by name, category and price range

def test_search_by_price_range():
    shop = SweetShop()
    shop.add_sweet(3, "Peda", "Pastry", 12.0, 10)
    results = shop.search_sweets(min_price=10 , max_price=15)
    assert len(results) == 1
    assert results[0]["name"] == "Peda"

# Test: Sorting sweets by price (ascending)

def test_sort_by_price():
    shop = SweetShop()
    shop.add_sweet(4, "Jalebi", "Candy", 20.0, 5)
    shop.add_sweet(5, "Kaju Katli", "Candy", 10.0, 5)
    sorted_sweets = shop.sort_sweets(by="price")
    assert sorted_sweets[0]["name"] == "Kaju Katli"

# Test: Sorting sweets by name (ascending)

def test_sort_by_name():
    shop = SweetShop()
    shop.add_sweet(5, "Kaju Katli", "Candy", 10.0, 5)
    shop.add_sweet(4, "Jalebi", "Candy", 20.0, 5)
    sorted_sweets = shop.sort_sweets(by="name")
    assert sorted_sweets[0]["name"] == "Jalebi"

# Test: Sorting sweets by quantity (ascending)

def test_sort_by_name():
    shop = SweetShop()
    shop.add_sweet(5, "Kaju Katli", "Candy", 10.0, 10)
    shop.add_sweet(4, "Jalebi", "Candy", 20.0, 5)
    sorted_sweets = shop.sort_sweets(by="quantity")
    assert sorted_sweets[0]["name"] == "Jalebi"

# Test: Purchasing a sweet and reducing quantity

def test_purchase_sweet():
    shop = SweetShop()
    shop.add_sweet(6, "Ladoo", "Pastry", 10.0, 10)
    shop.purchase_sweet("Ladoo", 3)
    sweet = shop.view_sweets()[0]
    assert sweet["quantity"] == 7

# Test: Trying to purchase more than in stock
# Should raise ValueError

def test_purchase_insufficient_stock():
    shop = SweetShop()
    shop.add_sweet(7, "Barfi", "Candy", 15.0, 2)
    with pytest.raises(ValueError, match="Not enough stock"):
        shop.purchase_sweet("Barfi", 5)


# Test: Restocking a sweet

def test_restock_sweet():
    shop = SweetShop()
    shop.add_sweet(8, "Gulab Jamun", "Pastry", 18.0, 5)
    shop.restock_sweet("Gulab Jamun", 10)
    sweet = shop.view_sweets()[0]
    assert sweet["quantity"] == 15

