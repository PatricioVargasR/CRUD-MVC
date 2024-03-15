# Importamos el módulo de webpy así como el modelo para las operaciones
import web
import base64
import hashlib
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

# Creamos un objeto Hash MD5
hash_md5 = hashlib.md5()

# Guardamos el tamaño máximo de una imagen
tamaño_maximo = 1048576

# Variable que almacena la ubicación de las vistas, con el argumento base es envuelto por una "plantilla"
render = web.template.render('mvc/views/', base='layout')

# Creamos una clase la cuál se encargará de manejar las peticiones POST y GET
class ActualizarProductos:

    def GET(self, idProducto):
        """
            Función que se encarga de renderizar la vista de actualizar_productos recibiendo como parámetro
            el identificador del producto
        """
        # Intentamos el siguiente bloque de código
        try:
            # Invocamos la función detalleProductos enviando como parámetro el indentificador del producto
            producto = PRODUCTO.detalleProductos(idProducto)
            # Renderizamos la vista correspondiente utilizando el producto de respuesta como parámetro
            return render.actualizar_productos(producto)
        # En caso de ocurrir algún error, muestra un mensaje en pantalla y en la consola el error
        except Exception as error:
            print(f'Ocurrió un error {error} - 105 | Controlador')
            return "Ocurrió un error"

    def POST(self, idProducto):
        """
            Función que se encarga de enviar datos obteniendolos de un formulario, en este caso son datos para
            actualizar un producto en la base de datos
        """
        # Intentamos el siguiente bloque de código
        try:
            # Obtenemos todos los valores del formulario y los guardamos en un diccionario, cada dato en su parte
            # correspondiente
            entrada = web.input(imagen = {})

            tamaño = len(entrada['imagen'].value)
            print(tamaño)

            # Obtenemos la extension de la imagen en caso de haberla
            if entrada['imagen'].value:
                extension = entrada['imagen'].filename.split('.')
                extension = extension[1]

            # Obtenemos el identificador y el hash de la URL
            antiguo_hash, identificador = idProducto.split('!')

            # Generamos la cadena a hashear:
            cadena = f"{entrada.nombre_producto}{entrada.descripcion}"
            # Actualizamos el objeto hash con los strings
            hash_md5.update(cadena.encode('utf-8'))
            # Obtenemos el hash md5 como string hexadecimal
            hash = hash_md5.hexdigest()
            # Verificamos que exista los datos de entrada, y que el identificador obtenido de la URL sea el mismo que del
            # formulario
            if entrada and entrada.producto == identificador and tamaño <= tamaño_maximo:
                producto =  {
                    "producto": entrada.producto,
                    "nombre":entrada.nombre_producto,
                    "descripcion":entrada.descripcion,
                    "imagen": base64.b64encode(entrada['imagen'].file.read()).decode('ascii'),
                    "extension": extension,
                    "precio":entrada.precio,
                    "existencia":entrada.existencia,
                    "antiguo_hash": antiguo_hash,
                    "hash": hash
                }
                # Invocamos la función para actualizarProductos enviando al diccionario como parámetro
                resultado = PRODUCTO.actualizarProductos(producto)
            # Verificamos que exista un resultado paara redireccionar a la página principal
            if resultado:
                web.seeother("/")
            else:
                return render.actualizar_productos(entrada.producto)

        # En caso de ocurrir algún error, muestra un mensaje en pantalla y en la consola el error
        except Exception as error:
            print(f'Ocurrió un error {error} - 105_2 | Controlador')
            return "Oucrrió un error"