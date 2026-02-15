# HomeWork 14.1
## Classes.py
Небольшая модель каталога товаров на Python с двумя классами: `Product` и `Category`. Подходит для образовательных примеров,
простых демонстраций предметной модели или как отправная точка для расширения в e‑commerce модуль.

## Содержание
- `product.py` — реализация классов `Product` и `Category`.
- `tests/` — (рекомендуется) тесты на `pytest`.

## Описание классов

### Product
- Поля:
  - `name` (str) — название товара.
  - `description` (str) — описание товара.
  - `price` (float) — цена.
  - `quantity` (int) — доступное количество.
- Конструктор:
  - `__init__(name, description, price, quantity)` — инициализирует поля без валидации.

### Category
- Поля:
  - `name` (str) — название категории.
  - `description` (str) — описание.
  - `products` (list[Product]) — список продуктов (сохраняется по ссылке).
  - `category_count` (int, class-level) — общее число созданных объектов `Category`.
  - `product_count` (int, class-level) — суммарное количество продуктов во всех категориях.
- Конструктор:
  - `__init__(name, description, products)` — присваивает поля и увеличивает class-level счётчики:
    - `Category.category_count += 1`
    - `Category.product_count += len(products)`

# HomeWork 16.1
- Были добавленны два дочерних класса Smartphone и LawnGrass от Product