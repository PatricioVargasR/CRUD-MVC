# Importamos los módulos correspondientes
import sqlite3
from typing import List, Dict, Union, Tuple

# Clase la cuál tendrá las operaciones que deseamos realizar
class ModeloProductos:

    def connect(self):
        """
            Función que se contecta a la base de datos y permite interactuar con ella con el cursor
            todas las clases siguientes la invocan
        """
        # Intentamos el siguiente bloque
        try:
            # Relizamos la conexión y creamos el cursor apartir de ella todo almacenandolo en la 'self'
            self.conn = sqlite3.connect('productos.db')
            self.cursor = self.conn.cursor()
        # En caso de ocurrir un error, regresar un mensaje en pantalla
        except sqlite3.Error as error:
            return f"Ocurrió un error {error}"

    def listaProductos(self) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de devolver todos los productos de la base de datos
            devuelve una lista con diccionarios dentro
        """
        # Inicializamos una lista para almacenar la respuesta
        response = []
        # Intentamos el siguiente bloque
        try:
            # Creamos la conexión y ejecutamos la sentencia SQL correspondiete
            self.connect()
            self.cursor.execute('SELECT * FROM productos ORDER BY id_productos DESC LIMIT 1')
            # Iteramos sobre el cursor, el cuál almacena el resultado para crear un diccionario de cada producto
            for row in self.cursor:
                product = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen": row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6],
                    "hash": row[7]
                    }
                # Guardamos cada diccionario de un producto en la lista
                response.append(product)
            self.conn.close()
        # En caso de ocurrir un error, imprime un mensaje en la consola y retorna la respuesta
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 201 | Modelo")
        return response

    def detalleProductos(self, idProducto: str) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de devolver los datos de un producto en base a su id
            devolviendo una lista con un diccionario del producto dentro
        """
        # Inicializamos una lista que almacenará la respuesta
        response = []
        # Intetamos el siguiente bloque de código
        try:
            # Creamos la conexión con la base de datosy realizamos la consulta para obtener el producto correspondiente
            self.connect()
            self.cursor.execute('SELECT * FROM productos WHERE hash = ? AND id_productos = ?', (idProducto.split('!')))
            # Iteramos sobre el cursor, el cuál almacena el resultado para crear un diccionario con el producto encontrado
            for row in self.cursor:
                product = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen":row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6]
                    }
                # Guardamos el diccionario del producto en la lista creada
                response.append(product)
            self.conn.close()
        # En caso de ocurrir algún error, imprime un mensaje en la consola y retorna la respuesta
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 202 | Modelo")
        return response

    def insertarProductos(self, producto: Dict[str, Union[int, float, str]]) -> bool:
        """
            Función que se encarga de insertar un nuevo producto en la base de datos, recibe un diccionario
            con los datos del producto correspondiete y devuelve un resultado booleano
        """
        # Inicializamos la variable de la respuesta
        respuesta = False
        # Intentamos el siguiente bloque de código
        try:
            # Creamos una nueva conexión y ejecutamos la función para insertar un nuevo producto con los datos
            # del JSON obtenido
            self.connect()
            self.cursor.execute('INSERT INTO productos (nombre, descripcion, imagen, extension, precio, existencias, hash) VALUES (?, ?, ?, ?, ?, ?, ?)', (producto["nombre"], producto["descripcion"], producto["imagen"], producto["extension"], float(producto["precio"]), int(producto["existencia"]), producto['hash']))
            # Guardamos el cambio ocurrio en la base de daots
            result = self.cursor.rowcount
            # En caso de haber un cambio, la variable de respuesta pasa a ser True
            if result:
                respuesta = True
            # Guardamos los cambios y cerramos la conexción
            self.conn.commit()
            self.conn.close()
        # En caso de ocurrir algún problema, imprimos el error correspondiente y delvolvemos la respuesta
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 203 | Modelo")
        return respuesta

    def actualizarProductos(self, producto: Dict[str, Union[int, float, str]]) -> bool:
        """
            Funciión que se encarga de actualizar un producto en la base de datos, recibe los datos actualizados
            del producto en un diccionario para luego ser subidos a la base de datos, devuelve una respuesta
            booleana
        """
        # Inicializamos una variable para la respuesta
        response = False
        # Intentamos el siguiente bloque de código
        try:
            # Creamos una nueva conexión con la base de datos y ejecutamos la consulta para actualizar el producto
            # los datos utilizados son los almacenados en el JSON
            self.connect()
            # Guardamos el cambio ocurrido en la base de datos
            self.cursor.execute("""UPDATE productos SET nombre = ?, descripcion = ?, imagen = ?, extension = ?,  precio = ?, existencias = ?, hash = ?
                                WHERE id_productos = ? AND hash = ?""", (producto["nombre"], producto["descripcion"], producto["imagen"], producto["extension"],
                                                            float(producto["precio"]), int(producto["existencia"]), producto["hash"], int(producto["producto"]), producto['antiguo_hash']))
            result = self.cursor.rowcount
            # En caso de existir algún cambio, la variable response para a ser True
            if result:
                response = True
            # Guardamos los cambios de la base de datos y cerramos la conexión.
            self.conn.commit()
            self.conn.close()
        # En caso de ocurrir algún error, imprime el error y devuelve la respuesta
        except sqlite3.Error as error:
            print(f"Ocurrió un error {error} - 204| Modelo")
        return response

    def borrarProductos(self, idProducto: str, hash: str) -> bool:
        """
            Función que se encarga de borrar un producto de la base de datos, recibe el identificador del producto
            a eliminar y devuelve un booleano
        """
        # Inicializamos la variable del resultado
        result = False
        # Intentamos el siguiente bloque de código
        try:
            # Creamos una nueva conexión y ejecutamos la consulta correspondiente para eliminar un producto en base al id
            # que obtiene la respuesta
            self.connect()
            self.cursor.execute('DELETE FROM productos WHERE id_productos = ? AND hash = ?', (idProducto, hash))
            # Guardamos los cambios realizamos en la base de datos
            filas_afectadas = self.cursor.rowcount
            # Guardamos las cambios realizamos en la base de datos y cerramos la conexión
            self.conn.commit()
            self.conn.close()
            # Si las filas afectadas son mayores que 0, la variable de resultado pasará a ser True
            if filas_afectadas > 0:
                result = True
        # En caso de ocurrir algún error, imprime el error ocurrido en la consola y devuelve el resultado
        except sqlite3.Error as error:
            print(f"Ocurrió un eror: {error} - 205 | Modelo")
        return result


    def buscarProductos(self, nombreProducto: str) -> Tuple[List[Dict[str, Union[int, float, str]]], bool]:
        """
            Función que se encarga de buscar un producto en base a su nombre, esta función no es sensible a mayúsculas
            ni a minúsculas, solamente al ordén y los espacios, recibe el nombre y devuelve el producto encontrado en un
            diccionario
        """
        # Inicializamos la variable para el resultado
        resultado = []
        # Inicializamos la variable buscado
        buscado = False
        # Intentamos el siguiente bloque de código
        try:
            # Creamos una nueva conexión y volvemos a minúsculas el nombre ingresado
            self.connect()
            nombreProducto = nombreProducto.lower()
            # Ejecutamos la sentencia SQL correspondiente para regresar el producto con más similitud
            self.cursor.execute('SELECT * FROM productos WHERE LOWER(nombre) LIKE ?', ('%' + nombreProducto + '%',))
            # Iteramos sobre el cursor el cuál almacena el resultado obtenido en la consulta anterior y lo guardamos
            # en un diccionario
            for row in self.cursor:
                producto = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen":row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6],
                    "hash": row[7]
                    }
                # Guardamos el diccionario dentro de una lista de la variable que inicializamos
                resultado.append(producto)
            if len(resultado) > 0:
                buscado = True
            self.conn.close()
        # En caso de ocurrir algún error, imprime en consola el error y devuelve el resultado
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 206 | Modelo")
        return (resultado, buscado)

    def paginacionProductos(self, por_pagina: int, offset: int) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de obtener los productos de la base de datos mediante los elementos por página y
            los elementos que se omiten, es decir, una manera de paginación. Esta función devolverá un array con los
            productos correspondientes a la página.
        """
        # Inicializamos la variable que almacena el resultado
        resultado = []
        # Intentamos el siguiente bloque de código
        try:
            # Creamos una nueva conexión y hacemos una consulta que delimita la cantidad de productos devuelvos y
            # los productos que se omiten
            self.connect()
            self.cursor.execute('SELECT * FROM productos ORDER BY id_productos DESC LIMIT ? OFFSET ?', (por_pagina, offset))
            # Iteramos sobre el cursor que almacena el resultado de la consulta anterior y lo convertimos a un JSON
            for row in self.cursor:
                product = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen": row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6],
                    "hash": row[7]
                    }
                # Guardamos los productos obtenidos en una lista y cerramos la conexión
                resultado.append(product)
            self.conn.close()
        # En caso de haber algún error, imprime en la consola el error
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 207 | Modelo ")
        return resultado

    def cantidadProductos(self) -> int:
        """
            Función que se encarga de devolver la cantidad de productos actuales almacenados en la base de datos, devuelve
            la cantidad exclusivamente.
        """
        # Inicializamos de la cantidad
        cantidad_productos = 0
        # Intentamos el siguiente bloque de código
        try:
            # Iniciamos una nueva colección y realizamos una consulta para obtener la cantidad de productos
            self.connect()
            self.cursor.execute('SELECT COUNT(*) as cantidad FROM productos')
            # Iteramos sobre el cursor que almacena el resultado de la consulta
            for row in self.cursor:
                cantidad = row[0]
            # Guardamos la nueva cantidad de productos y cerramos la conexión
            cantidad_productos = cantidad
            self.conn.close()
        # En caso de haber algún error, imprime en la consola el error
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 208 | Modelo ")
        return cantidad_productos