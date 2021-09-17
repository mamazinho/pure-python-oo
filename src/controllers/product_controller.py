from src.daos.product_dao import ProductDAO

from src.daos.category_dao import CategoryDAO

from src.daos.product_category_dao import ProductCategoryDao

from src.models.product_model import Product


"""
This class serves to control the data between user inputs and all the other 
DAOs.
"""


class ProductController:

    def __init__(self):
        self.product_dao = ProductDAO()
        self.category_dao = CategoryDAO()
        self.product_category_dao = ProductCategoryDao()

    def create(self, product:dict):
        new_product = Product(
            product['name'],
            product['description'],
            product['price'],
            product['categories']
        )
        product['id'] = self.product_dao.create(new_product)
        self.__create_product_category(product)

    def read(self):
        products = self.product_dao.read_all()
        return products

    def read_by_id(self, id:int):
        return self.product_dao.read_by_id(id)

    def update(self, product:dict):
        categories = product.get('categories', None)

        updated_product = Product(
            product['name'],
            product['description'],
            product['price'],
            categories,
            product['id']
        )

        if categories:
            self.__create_product_category(product)

        self.product_dao.update(updated_product)

    def delete(self, id:int):
        self.product_dao.delete(id)

    def get_categories(self):
        categories = self.category_dao.read_all()
        return categories

    def __create_product_category(self, product:dict):
        for selected_category in product['categories']:
            self.product_category_dao.create(
                product['id'], selected_category)