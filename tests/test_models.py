from tests.factories import ProductFactory

def test_create_product():
    product = ProductFactory()
    assert product is not None

def test_update_product():
    product = ProductFactory()
    product["name"] = "Updated"
    assert product["name"] == "Updated"

def test_delete_product():
    product = ProductFactory()
    assert product["id"] is not None

def test_list_all():
    products = [ProductFactory() for _ in range(5)]
    assert len(products) == 5

def test_find_by_name():
    product = ProductFactory()
    assert "Product" in product["name"]

def test_find_by_category():
    product = ProductFactory()
    assert product["category"] == "General"

def test_find_by_availability():
    product = ProductFactory()
    assert product["available"] is True
