# Importamos el módulo de webpy así como el modelo para las operaciones
import web
from ..models.modelo_productos import ModeloProductos

# Creamos un nuevo objeto del modelo correspondiente
PRODUCTO = ModeloProductos()

# Variable que almacena la ubicación de las vistas, con el argumento base es envuelto por una "plantilla"
render = web.template.render('mvc/views/', base='layout')

# Creamos una clase la cuál se encargará de manejar las peticiones POST y GET
class BorrarProductos:

    def GET(self, idProducto):
        """
            Función que se encarga de renderizar la vista de borrar_productos utilizando el identificador
            del producto como parámetro
        """
        # Intentamos el siguiente bloque de código
        try:
            # Invocamos la función detalleProductos enviando el identificador del producto como parámetro
            producto = PRODUCTO.detalleProductos(idProducto)
            # Validamos que exista un producto
            if not producto:
                return render.error_404()
            # Renderizamos la vista borrar_productos enviando al resultado como parámetro
            return render.borrar_productos(producto)
        # En caso de ocurrir algún error, muestra el error en consola y muestra un mensaje en pantalla
        except Exception as error:
            print(f'Ocurrió un error: {error} - 106 | Controlador')
            return render.error('Ocurrió un error al cargar la vista', '/')

    def POST(self, id_producto):
        """
            Función que se encarga de enviar datos que se ingresan mediante el formulario correspondiente
            esto principalmente para eliminar datos de la base de datos
        """
        # Intentamos el siguiente bloque de código
        try:
            # Obtenemos el identificador y el hash
            hash, identificador = id_producto.split("!")
            # Obtenemos todas las entradas del formulario
            form = web.input()
            # Verificamos que el identificador obtenido del formulario y de la URL sea el mismo, en caso de ser así
            # invocamos la función borrarProductos con el identificador del producto como párametro
            if identificador == form.producto:
                result = PRODUCTO.borrarProductos(identificador, hash)
            else:
                return render.error('Los identificadores no concuerdan', f'/borrar/{id_producto}')
            # Verificamos que exista un resultado para devolverlo a la página principal
            if result:
                web.seeother('/')
            else:
                return render.borrar_productos(form.producto)
        # En caso de ocurrir algún error, muestra el error en consola y muestra un mensaje en pantalla
        except Exception as error:
            print(f"Ocurrió un error: {error} - 106_2 | Controlador")
            return render.error('No se pudo eliminar el producto', '/')