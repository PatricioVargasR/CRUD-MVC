# Importamos el módulo de webpy así como el modelo para las operaciones
import web
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

# Variable que almacena la ubicación de las vistas, con el argumento base es envuelto por una "plantilla"
render = web.template.render('mvc/views/', base='layout')

# Creamos una clase la cuál se encargará de manejar las peticiones GET
class DetalleProductos:

    def GET(self, idProductos):
        """
            Función que se encarga de renderizar la vista de detall_productos, esto utilizando como parámetro
            el identificador del producto
        """
        # Intentamos el siguiente bloque de código
        try:
            # Invocamos la función detalleProductos enviando el identificador del producto como parámetro
            producto = PRODUCTO.detalleProductos(idProductos)
            # Renderizamos la vista correspondiente enviando el resultado como parámetro
            return render.detalle_productos(producto)
        # En caso de que ocurriera algún error, imprime en consolta el error y muestra un mensaje en la pantalla
        except Exception as error:
            print(f'Ocurrió un error {error} - 103 | Controlador')
            return 'Ocurrió un error'