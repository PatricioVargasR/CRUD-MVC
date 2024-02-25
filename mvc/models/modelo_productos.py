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
                product = {
                    "id_productos":row[0],
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


    def detalleProductos(self, idProducto: str) -> List[Dict[str, Union[int, float, str]]]:
        response = []
        try:
            self.connect()
            self.cursor.execute('SELECT * FROM productos WHERE id_productos = ?', (idProducto, ))
            for row in self.cursor:
                product = {
                    "id_producto": row[0],
                    "nombre":row[1],
                    "descripción": row[2],
                    "precio":row[3],
                    "existencias": row[4]
                }
                response.append(product)
            self.conn.close()
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 202 | Modelo")
        return response

    def insertarProductos(self, producto: Dict[str, Union[int, float, str]]) -> bool:
        respuesta = False
        try:
            self.connect()
            self.cursor.execute('INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES (?, ?, ?, ?)', (producto["nombre"], producto["descripcion"], float(producto["precio"]), int(producto["existencia"])))
            result = self.cursor.rowcount
            if result:
                respuesta = True
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 203 | Modelo")
        return respuesta

    def actualizarProductos(self, producto: Dict[str, Union[int, float, str]]) -> bool:
        response = False
        try:
            self.connect()
            print(producto)
            self.cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, existencias = ? WHERE id_productos = ?", (producto["nombre"], producto["descripcion"], producto["precio"], producto["existencia"], int(producto["producto"])))
            result = self.cursor.rowcount
            if result:
                response = True
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as error:
            print(f"Ocurrió un error {error} - 204| Modelo")
        return response

    def borrarProductos(self, idProducto: str) -> bool:
        result = False
        try:
            self.connect()
            self.cursor.execute('DELETE FROM productos WHERE id_productos = ?', (idProducto, ))
            filas_afectadas = self.cursor.rowcount
            self.conn.commit()
            self.conn.close()
            if filas_afectadas > 0:
                result = True
        except sqlite3.Error as error:
            print(f"Ocurrió un eror: {error} - 205 | Modelo")
        return result


    def buscarProductos(self, nombreProducto: str) -> List[Dict[str, Union[int, float, str]]]:
        resultado = []
        try:
            self.connect()
            nombreProducto = nombreProducto.lower()

            self.cursor.execute('SELECT * FROM productos WHERE LOWER(nombre) LIKE ?', ('%' + nombreProducto + '%',))
            for row in self.cursor:
                producto = {
                    "id_productos": row[0],
                    "nombre":row[1],
                    "descripción": row[2],
                    "precio":row[3],
                    "existencias": row[4]
                }
                resultado.append(producto)
            self.conn.close()
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 206 | Modelo")
        return resultado

    def creditos(self):
        try:
            pass
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 207 | Modelo")