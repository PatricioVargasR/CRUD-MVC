# Importamos los módulos correspondientes
import sqlite3
from typing import List, Dict, Union

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
            self.cursor.execute('SELECT * FROM productos')
            # Iteramos sobre el cursor, el cuál almacena el resultado para crear un diccionario de cada producto
            for row in self.cursor:
                product = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "precio":row[3],
                    "existencias":row[4]
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
            self.cursor.execute('SELECT * FROM productos WHERE id_productos = ?', (idProducto, ))
            # Iteramos sobre el cursor, el cuál almacena el resultado para crear un diccionario con el producto encontrado
            for row in self.cursor:
                product = {
                    "id_producto": row[0],
                    "nombre":row[1],
                    "descripción": row[2],
                    "precio":row[3],
                    "existencias": row[4]
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
            self.cursor.execute('INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES (?, ?, ?, ?)', (producto["nombre"], producto["descripcion"], float(producto["precio"]), int(producto["existencia"])))
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
            self.cursor.execute("UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, existencias = ? WHERE id_productos = ?", (producto["nombre"], producto["descripcion"], producto["precio"], producto["existencia"], int(producto["producto"])))
            # Guardamos el cambio ocurrido en la base de datos
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

    def borrarProductos(self, idProducto: str) -> bool:
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
            self.cursor.execute('DELETE FROM productos WHERE id_productos = ?', (idProducto, ))
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


    def buscarProductos(self, nombreProducto: str) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de buscar un producto en base a su nombre, esta función no es sensible a mayúsculas
            ni a minúsculas, solamente al ordén y los espacios, recibe el nombre y devuelve el producto encontrado en un
            diccionario
        """
        # Inicializamos la variable para el resultado
        resultado = []
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
                    "id_productos": row[0],
                    "nombre":row[1],
                    "descripción": row[2],
                    "precio":row[3],
                    "existencias": row[4]
                }
                # Guardamos el diccionario dentro de una lista de la variable que inicializamos
                resultado.append(producto)
            self.conn.close()
        # En caso de ocurrir algún error, imprime en consola el error y devuelve el resultado
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 206 | Modelo")
        return resultado

    def creditos(self):
        try:
            pass
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 207 | Modelo")