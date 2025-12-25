import unittest
from main import Category, Product


class TestProduct(unittest.TestCase):
    def test_init(self):

        p = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

        self.assertEqual(p.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(p.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(p.price, 180000.0)
        self.assertEqual(p.quantity, 5)


class TestCategory(unittest.TestCase):
    def test_init(self):

        product_list = [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ]

        cat = Category("Смартфоны", "Описание смартфонов", product_list)

        self.assertEqual(cat.name, "Смартфоны")
        self.assertEqual(cat.description, "Описание смартфонов")

        self.assertListEqual(cat.products, product_list)

        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, len(product_list))  # Количество продуктов совпадает с длиной списка


if __name__ == "__main__":
    unittest.main()
