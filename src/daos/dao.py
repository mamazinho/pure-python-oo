from .database import Database

from typing import NoReturn

"""
This class abstracts all connections with database to execute the queries
passed by specific DAOs
"""


class Dao:


    def insert_data(self, sql:str, parameters:tuple) -> int :      
        with Database() as conn:
            cursor = conn.cursor() 
            cursor.execute(sql,parameters)
            conn.commit()
            id = cursor.lastrowid
        return id

    def execute_query(self, sql:str, parameters:tuple=None) -> NoReturn:
        with Database() as conn:
            cursor = conn.cursor() 
            if parameters:    
                cursor.execute(sql, parameters)
            else:
                cursor.execute(sql)
            conn.commit()


    def execute_query_select(self, sql:str, parameters:tuple=None) -> tuple:
        with Database() as conn:
            cursor = conn.cursor()  
            result = ()
            if parameters:   
                cursor.execute(sql, parameters)
            else:
                cursor.execute(sql)

            result = cursor.fetchall()

        return result
    