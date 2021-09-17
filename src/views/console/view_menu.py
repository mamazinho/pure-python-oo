import os

from .product_view import ProductView
from .category_view import CategoryView

modules = {
    '1': 'Product',
    '2': 'Category',
    '0': 'Sair'
}
crud_option = {
    '1' : 'Create',
    '2' : 'Read',
    '3' : 'Update',
    '4' : 'Delete',
    '0' : 'Voltar'
}

class ViewMenu:

    def __init__(self):
        self.module = None


    def execute(self):
        self.set_screen(modules, f"{' '*20} Modulo Principal {' '*20}", False)
    
    def set_screen(self, menu, message, sub_menu):
        valid = False
        choice = None
        while not valid:
            self.print_menu(menu, message)
            choice = self.get_choice()  
            valid = self.valid_choice(choice, menu)
            if choice != '0' and valid:
                if sub_menu:
                    self.crud(choice)
                else:
                    self.get_module(modules[choice])
                    self.set_screen(crud_option, f"{' '*20} Modulo de {modules[choice]} {' '*20}", True)    
                 
    def get_module(self, module):
        self.module = ProductView() if module == 'Product' else CategoryView()


    def print_menu(self, menu, message):
        os.system('clear')
        print("="*20, "Bem vindos ao olist !", "="*20, '\n')
        print(message, '\n')
        for c,v in menu.items():
            print(f"\t{c} - {v}")

    def get_choice(self):
        choice = input("\nEscolha uma das opções do menu:")
        return choice            
    
    def valid_choice(self, choice, menu):
        if choice in menu.keys():
            return True
        return False    

    def crud(self, choice):
        if choice == '1':
            #create
            self.module.create()
        elif choice == '2':
            #read
            self.module.read()
        elif choice == '3':
            #update
            self.module.update()
        elif choice == '4':
            #delete
            self.module.delete()
