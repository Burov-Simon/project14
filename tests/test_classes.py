import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


def test_product_initialization():
    p = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert p.name == "Samsung Galaxy S23 Ultra"
    assert p.description == "256GB, Серый цвет, 200MP камера"
    assert p.price == 180000.0
    assert p.quantity == 5


product1 = Product(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_category_initialization():
    c = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации",
        [product1, product2],
    )
    assert c.name == "Смартфоны"
    assert c.description == "Смартфоны, как средство не только коммуникации"
    assert c.products == [
        "Samsung Galaxy S23 Ultra: 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15: 210000.0 руб. Остаток: 8 шт.",
    ]
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_product_creation_and_price(capsys):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product.price = 800
    assert new_product.price == 800
    new_product.price = 0
    message = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in message.out
    new_product.price = -100
    assert "Цена не должна быть нулевая или отрицательная" in message.out


@pytest.fixture
def category_smart():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни.",
        [product1, product2],
    )


def test_add_product_category(category_smart):
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category.add_product(category_smart, product4)
    assert category_smart.product_count == 5


def test_str_product():
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product():
    assert product1 + product2 == 2580000.0


def test_str_category(category_smart):
    assert str(category_smart) == "Смартфоны, количество продуктов: 13 шт."


def test_smartphone_init():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_lawngrass_init():
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_add_product_error():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )

    with pytest.raises(TypeError):
        category_smartphones.add_product("smartphone2")


def test_add_product_invalid():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_mixin_print(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    messages = capsys.readouterr()
    assert (
        messages.out.strip()
        == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )


def test_value_error_in_product():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_category_middle_price(category_smart):
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
    assert category_smart.middle_price() == 195000.0
