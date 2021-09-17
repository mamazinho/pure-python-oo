from src.controllers.category_controller import CategoryController
from src.utils.utils import format_print

class CategoryView:
    def __init__(self):
        self.controller = CategoryController()
        self.category = {
            'id': 0,
            'name': '',
            'description': '',
            'products': []
        }

    def create(self):
        self.category['name'] = input("Escreva o nome da categoria:")
        self.category['description'] = input("Escreva a descrição da categoria:")
        self.controller.create(self.category)

    def read(self):
        categories = self.controller.read()
        format_print(categories)

    def update(self):
        self.read()
        self.category['id'] = input("Escolha uma categoria para editar:")
        self.category['name'] = input("Escreva o novo nome da categoria:")
        self.category['description'] = input("Escreva a nova descrição da categoria:")
        self.controller.update(self.category)

    def delete(self):
        self.read()
        self.category['id'] = input('escolha uma categoria que deseja deletar:')
        self.controller.delete(self.category['id'])