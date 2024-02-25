import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()

render = web.template.render('mvc/views/', base='layout')

class BorrarProductos:

    def GET(self, idProducto):
        try:
            producto = PRODUCTO.detalleProductos(idProducto)
            print(producto)
            return render.borrar_productos(producto)
        except Exception as error:
            print(f'Ocurrió un error: {error} - 106 | Controlador')
            return "Ocurrió un error"

    def POST(self, id_producto):
        try:
            form = web.input()
            if id_producto == form.producto:
                result = PRODUCTO.borrarProductos(id_producto)
            if result:
                web.seeother('/')
        except Exception as error:
            print(f"Ocurrió un error: {error} - 106_2 | Controlador")
            return "Ocurrió un error"