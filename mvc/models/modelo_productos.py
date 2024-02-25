import sqlite3
from typing import List, Dict, Union

class ModeloProductos:

    def connect(self):
        try:
            self.conn = sqlite3.connect('productos.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            return f"Ocurrió un error {error}"

    def listaProductos(self) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de devolver todos los productos de la base de datos
        """
        response = []
        try:
            self.connect()
            self.cursor.execute('SELECT * FROM productos')
            for row in self.cursor:
                print(row[1])
                product = {
                    "nombre":row[1],
                    "descripción":row[2],
                    "precio":row[3],
                    "existencias":row[4]
                    }
                response.append(product)
            self.conn.close()
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 201 | Modelo")
        return response

    def creditos(self):
        try:
            pass
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 202 | Modelo")

    def detalleProductos(self):
        try:
            pass
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 203 | Modelo")

    def insertarProductos(self):
        try:
            pass
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 204 | Modelo")

    def actualizarProductos(self):
        try:
            pass
        except sqlite3.Error as error:
            print(f"Ocurrió un error {error} - 205 | Modelo")