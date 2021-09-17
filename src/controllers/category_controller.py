from src.daos.category_dao import CategoryDAO

from src.models.category_model import Category


"""
This class serves to control the data between user inputs and category DAO
"""


class CategoryController:

    def __init__(self):
        self.category_dao = CategoryDAO()

    # def create(self, name, description):
    #     new_category = Category(
    #         name,
    #         description
    #     )
    #     category_id = self.category_dao.create(new_category)
    #     return category_id

    def create(self, category:dict):
        new_category = Category(
            category['name'],
            category['description']
        )
        category_id = self.category_dao.create(new_category)
        return category_id

    def read(self):
        categories = self.category_dao.read_all()
        return categories

    def read_by_id(self, id:int):
        return self.category_dao.read_by_id(id)

    # def update(self, category_id, name, description):

    #     updated_category = Category(
    #         name,
    #         description,
    #         category_id
    #     )

    #     self.category_dao.update(updated_category)

    def update(self, category:dict):

        updated_category = Category(
            category['name'],
            category['description'],
            category['id']
        )

        self.category_dao.update(updated_category)

    def delete(self, id:int):
        self.category_dao.delete(id)
