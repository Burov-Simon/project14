import pytest
from src.classes import Product, Category



def test_product_initialization():
    p = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert p.name == "Samsung Galaxy S23 Ultra"
    assert p.description == "256GB, Серый цвет, 200MP камера"
    assert p.price == 180000.0
    assert p.quantity == 5


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_category_initialization():
    c = Category("Смартфоны",
                 "Смартфоны, как средство не только коммуникации",
                 [product1, product2])
    assert c.name == "Смартфоны"
    assert c.description == "Смартфоны, как средство не только коммуникации"
    assert c.products == [product1, product2]
    assert Category.category_count == 1
    assert Category.product_count == 2