# Importamos el módulo de webpy así como el modelo para las operaciones
import web
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

# Variable que almacena la ubicación de las vistas, con el argumento base es envuelto por una "plantilla"
render = web.template.render('mvc/views/', base='layout')

# Creamos una clase la cuál se encargará de manejar las peticiones POST y GET
class PaginacionProductos:

    def GET(self, pagina=2):
        """
            Función que se encarga de renderizar la vista de paginación_productos enviando como parámetro los productos
            obtenidos de la función de paginacionProductos del modelo
        """
        # Intentamos el siguiente bloque de código
        try:
            # Convertimos el parámetro de la url
            pagina = int(pagina)
            # Definimos los items por página
            por_pagina = 1
            # Definimos la cantidad de items a saltarse
            offset = (pagina - 1) * por_pagina

            # Calculamos los elementos que se omiten en cada página
            productos = PRODUCTO.paginacionProductos(por_pagina, offset)
            # Invocamos la función cantidadProductos del modelo y guardamos su resultado en una variable
            cantidad_productos = PRODUCTO.cantidadProductos()

            # Obtenemos el total de las páginas
            paginas =  cantidad_productos // por_pagina
            # Aumentamos la cantidad de páginas siempre y cuando cumplan la condición
            if cantidad_productos % pagina == 1:
                paginas += 1

            # Verificamos la cantidad de páginas
            if pagina > paginas:
                web.seeother("/")
            else:
                # Renderizamos la vista correspondiente con los productos cómo argumento
                return render.paginacion_productos(productos, pagina, int(paginas))
        # En caso de ocurrir algún error, imprime el error en pantalla y regresa un mensaje
        except Exception as error:
            print(f"Ocurrió un error {error} - 106 | Controlador")
            return "Ocurrió un error"

    def POST(self, pagina=2):
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
                respuesta, busqueda = PRODUCTO.buscarProductos(producto_buscado)
            # Verificamos que exista una respuesta para renderizar la vista con los datos del producto encontrado
            # en caso de no existir un producto, regresa a la página principal
            if respuesta:
                return render.lista_productos(respuesta, busqueda)
            else:
                web.seeother("/")
        # En caso de ocurrir algún error imprime el error en consola y devuelve un mensaje en pantalla
        except Exception as error:
            print(f"Ocurrió un error {error} - 106_2 | Controlador")
            return "Ocurrió un error"