from src.controllers.product_controller import ProductController

from src.utils.utils import format_print


class ProductView:

    def __init__(self):
        self.controller = ProductController()
        self.product = {
            'id': 0,
            'name': '',
            'description': '',
            'price': 0.0,
            'categories': []
        }

    def create(self):
        self.product['name'] = input("\nEscreva o nome do produto: ")
        self.product['description'] = input(
            "\nEscreva a descrição do produto: ")
        self.product['price'] = input("\nEscreva o preço do produto: ")

        self.__get_categories()
        self.controller.create(self.product)

    def read(self):
        products = self.controller.read()
        format_print(products)

    def update(self):
        self.read()
        self.product['id'] = input("Qual o id do produto a ser atualizado? ")
        self.product['name'] = input("Qual o novo nome do produto? ")
        self.product['description'] = input(
            "Qual a nova descrição do produto? ")
        self.product['price'] = input("Qual o novo preço do produto? ")
        more_categories = input(
            "Deseja adicionar categorias ao produto? (s/N) ")

        
        if more_categories == "s":
            self.__get_categories()

        self.controller.update(self.product)

    def delete(self):
        self.read()
        self.product['id'] = input("Qual o id do produto a ser removido? ")
        self.controller.delete(self.product['id'])

    def __get_categories(self):
        while True:
            print("\nSelecione uma das categorias abaixo:\n")
            categories = self.controller.get_categories()
            format_print(categories)
            selected_category = input()
            self.product['categories'].append(selected_category)
                
            option = input("\nVocê deseja cadastrar mais uma categoria? (s/N)")
            if option == "s":
                continue
            else:
                break