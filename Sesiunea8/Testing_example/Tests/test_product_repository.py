from Sesiunea8.Testing_example.App.product import Product
from Sesiunea8.Testing_example.App.product_repository import ProductRepository
import unittest
from parameterized import parameterized


class TestProductRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = ProductRepository()

    def test_get_all(self):
        # repo = ProductRepository()
        self.assertEqual(self.repo.products, self.repo.get_all())

    @parameterized.expand([
        ("Orez", Product(name="Orez", price=4.5, discount=10, category="Alimente de baza")),
        ("Vin", None)
    ])
    def test_get_by_name(self, name, expected):
        self.repo = ProductRepository()
        self.assertEqual(expected, self.repo.get_by_name(name))
