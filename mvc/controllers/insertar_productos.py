# Importamos el módulo de webpy así como el modelo para las operaciones
import web
import base64
import hashlib
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

# Creamos un objeto Hash MD5
hash_md5 = hashlib.md5()

# Guardamos el tamaño máximo de la imagen
tamaño_maximo = 1048576
# Variable que almacena la ubicación de las vistas, con el argumento base es envuelto por una "plantilla"
render = web.template.render('mvc/views/', base='layout')

# Creamos una clase la cuál se encargará de manejar las peticiones POST y GET
class InsertarProductos:

    def GET(self):
        """
            Función que se encarga de renderizar la vista de insertar_productos, el cuál es un formulario
            para obtener los datos
        """
        # Intentamos el siguiente bloque de código
        try:
            # Renderizamos la vista correspondiente
            return render.insertar_productos()
        # En caso de ocurrir algún error, imprime el error en la consola y manda un mensaje en pantalla
        except Exception as error:
            print(f'Ocurrió un error: {error} - 104 | Controlador')
            return render.error('No se pudo cargar la vista', '/')

    def POST(self):
        """
            Función que se encarga de enviar datos, en este caso obtiene los datos del formulario para insertar
            productos
        """
        # Intentamos el siguiente bloque de código
        try:
            # Obtenemos todas las entradas del formuarlio
            entrada = web.input(imagen = {})

            # Validamos en caso de no haber datos ingresados
            if not entrada['precio'] or not entrada['nombre_producto'] or not entrada['existencia'] or not entrada['descripcion']:
                return render.error('No completó todos los campos', '/insertar')

            # Validamos en caso de no haber imagen de la imagen
            if len(entrada['imagen'].value) <= 0:
                return render.error('No insertó la imagen', '/insertar')

            # Obtenemos la extesión de la imagen
            extension = entrada['imagen'].filename.split('.')
            # Obtenemos el tamaño de la imagen
            tamaño = len(entrada['imagen'].value)

            # Validamos el tamaño de la imagen
            if tamaño >= tamaño_maximo:
                return render.error('El tamaño de la imagen excede lo permitido', '/insertar')

            # Validamos las existencias y el precio
            if float(entrada.precio) <= 0 or int(entrada.existencia) < 0:
                return render.error('No se permite precios nulos ni existencias menores que cero', '/insertar')

            # En caso de de hubiera una entrada guardamos cada entrada especifica en su campo correspondiente
            if entrada:
                # Generamos la cadena a hashear:
                cadena = f"{entrada.nombre_producto}{entrada.descripcion}"
                # Actualizamos el objeto hash con los strings
                hash_md5.update(cadena.encode('utf-8'))
                # Obtenemos el hash md5 como string hexadecimal
                hash = hash_md5.hexdigest()
                producto =  {
                    "nombre":entrada.nombre_producto,
                    "descripcion":entrada.descripcion,
                    "imagen": base64.b64encode(entrada['imagen'].file.read()).decode('ascii'),
                    "extension": extension[1],
                    "precio":entrada.precio,
                    "existencia":entrada.existencia,
                    "hash": hash
                }
                # Invocamos la función insertarProductos la cuál recibe como parámetro el diccionario del producto
                resultado = PRODUCTO.insertarProductos(producto)
            # En caso de haber un resultado, se redirecciona a la pantalla principal
            if resultado:
                web.seeother("/")
            else:
                return render.insertar_productos()
        # En caso de ocurrir algún error, imprime el error en la consolta y manda un mensaje en pantalla
        except Exception as error:
            print(f"Ocurrió un error: {error} - 104_2 | Controlador")
            return render.error('No se logró insertar el nuevo producto', '/')
