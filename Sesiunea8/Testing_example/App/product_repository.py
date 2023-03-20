from Sesiunea8.Testing_example.App.product import Product
class ProductRepository:
    products = [
        Product(name="Orez", price=4.5, discount=10, category="Alimente de baza"),
        Product(name="Paine neagra", price=3.79, discount=0, category="Fainoase"),
        Product(name="Faina integrala", price=1.85, discount=5, category="Fainoase"),
        Product(name="Zahar brun", price=6.5, discount=0, category="Alimente de baza"),
        Product(name="Oua", price=14.79, discount=5, category="Alimente de baza"),
        Product(name="Branza de capra", price=14.99, discount=10, category="Lactate"),
        Product(name="Apa plata", price=2.09, discount=33, category="Bauturi"),
        Product(name="Apa minerala", price=2.3, discount=33, category="Bauturi"),
        Product(name="Bere", price=3.5, discount=15, category="Bauturi"),
        Product(name="Ovaz", price=1.99, discount=0, category="Alimente de baza"),
    ]

    def get_all(self):
        return self.products

    def get_by_name(self,name):
        for product in self.products:
            if product.name == name:
                return product