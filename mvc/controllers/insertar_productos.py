# Importamos el módulo de webpy así como el modelo para las operaciones
import web
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

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
            return "Ocurrió un error"

    def POST(self):
        """
            Función que se encarga de enviar datos, en este caso obtiene los datos del formulario para insertar
            productos
        """
        # Intentamos el siguiente bloque de código
        try:
            # Obtenemos todas las entradas del formuarlio
            entrada = web.input()
            # En caso de de hubiera una entrada guardamos cada entrada especifica en su campo correspondiente
            if entrada:
                producto =  {
                    "nombre":entrada.nombre_producto,
                    "descripcion":entrada.descripcion,
                    "precio":entrada.precio,
                    "existencia":entrada.existencia
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
            return "Ocurrió un error"