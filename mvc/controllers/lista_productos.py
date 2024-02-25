# Importamos el módulo de webpy así como el modelo para las operaciones
import web
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

# Variable que almacena la ubicación de las vistas, con el argumento base es envuelto por una "plantilla"
render = web.template.render('mvc/views/', base='layout')

# Creamos una clase la cuál se encargará de manejar las peticiones POST y GET
class ListaProductos:

    def GET(self):
        """
            Función que se encarga de renderizar la vista de lista_productos enviando como parámetro los productos
            obtenidos de la función de listaProductos del módelo
        """
        # Intentamos el siguiente bloque de código
        try:
            # Invocamos la función listaProductos del modelo y guardamos su resultado en una variable
            productos = PRODUCTO.listaProductos()
            # Renderizamos la vista correspondiente con los productos cómo argumento
            return render.lista_productos(productos)
        # En caso de ocurrir algún error, imprime el error en pantalla y regresa un mensaje
        except Exception as error:
            print(f"Ocurrió un error {error} - 101 | Controlador")
            return "Ocurrió un error"

    def POST(self):
        """
            Función que se encarga de enviar datos ingresados en formularios de esta vista, principalmente utilizada
            para buscar los productos
        """
        # Intentamos el siguiente bloque de código
        try:
            # Obtenemos todas las entradas del formulario y almacenamos el datos "nombre" dentro de una variable
            entrada = web.input()
            producto_buscado = entrada.nombre
            # Verificamos la existencia de datos y del producto correspondiente para luego invocar la función
            # buscarProductos enviando el nombre del producto como parámetro
            if entrada and producto_buscado:
                respuesta = PRODUCTO.buscarProductos(producto_buscado)
            # Verificamos que exista una respuesta para renderizar la vista con los datos del producto encontrado
            # en caso de no existir un producto, regresa a la página principal
            if respuesta:
                return render.lista_productos(respuesta)
            else:
                web.seeother("/")
        # En caso de ocurrir algún error imprime el error en consola y devuelve un mensaje en pantalla
        except Exception as error:
            print(f"Ocurrió un error {error} - 101_2 | Controlador")
            return "Ocurrió un error"