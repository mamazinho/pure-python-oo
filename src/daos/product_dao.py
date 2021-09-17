from src.daos.dao import Dao

from src.models.product_model import Product


"""
This class makes a communication between product controller data and
set the queries to save product table on database.
"""


class ProductDAO(Dao):

    def __init__(self):
        self.create_table()

    def create_table(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL,
            price REAL NOT NULL
            );
        """)

    def create(self, product):
        sql = """
        INSERT INTO product (name, description, price) VALUES (?, ?, ?)
        """
        parameters = (product.name, product.description, product.price)
        return self.insert_data(sql, parameters)

    def read_all(self):
        sql = """
        SELECT product.id, product.name, product.description, product.price, group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        GROUP BY product.name, product.description, product.price
        ORDER BY product.id
        """

        list_products = []
        result = self.execute_query_select(sql)

        for item in result:
            product = Product(item[1], item[2], item[3], item[4], item[0])
            list_products.append(product)

        return list_products

    def read_by_id(self, id: int):
        sql = """
        SELECT product.id, product.name, product.description, product.price, group_concat(category.id), group_concat(category.name)
        FROM product JOIN product_category ON product_id = product.id JOIN category ON category_id = category.id
        WHERE product.id = ?
        GROUP BY product.name, product.description, product.price
        ORDER BY product.id
        """
        parameter = (id, )

        result = self.execute_query_select(sql, parameter)
        item = result[0]

        product = Product(item[1], item[2], item[3], [item[4], item[5]], item[0])
        return product

    def update(self, product):
        sql = """
            UPDATE product
                SET
                    name = ?
                    ,description = ?
                    ,price = ?
                WHERE id = ?
        """
        parameters = (product.name, product.description,
                      product.price, product.id)

        return self.execute_query(sql, parameters)

    def delete(self, id: int):
        sql = """
            DELETE FROM product
                WHERE id = ?
        """
        parameters = (id, )

        return self.execute_query(sql, parameters)
