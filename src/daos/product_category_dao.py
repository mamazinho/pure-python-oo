from src.daos.dao import Dao


"""
This class makes a communication between product controller data and
set the queries to save in product_category table on database.
"""


class ProductCategoryDao(Dao):

    def __init__(self):
        self.create_table()

    def create_table(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS product_category (
            product_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY(product_id) REFERENCES product(id),
            FOREIGN KEY(category_id) REFERENCES category(id),
            PRIMARY KEY(product_id, category_id)            
            );
        """)

    def create(self, product_id:int, category_id:int) -> int:
        sql = """
        INSERT OR IGNORE INTO product_category (product_id, category_id) VALUES (?, ?)
        """
        parameters = (product_id, category_id)

        id = self.insert_data(sql, parameters)
        return id
