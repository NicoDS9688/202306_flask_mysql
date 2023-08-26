"""MYSQLCONNECTION"""

import os

import pymysql.cursors


class MySQLConnection:
    """Crea instancia de conexión a base de datos."""
    def __init__(self, db):
        connection = pymysql.connect(
            host="localhost",
            user=os.getenv('DATABASE_USER'),
            password='',
            db=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )
        self.connection = connection


    def query_db(self, query, data=None):
        """Método para consultar la base de datos."""
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Consulta SQL EJECUTADA:", query)
                cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("AN ERROR HAS OCURRED ----->", e)
                return False
            finally:

                self.connection.close()


def connectToMySQL(db):
    """Método que recibe la base de datos utilizada y la usa para crear
      una instancia de MySQLConnection"""
    return MySQLConnection(db)
