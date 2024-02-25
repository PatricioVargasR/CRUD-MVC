import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()

render = web.template.render('mvc/views/', base='layout')

class ActualizarProductos:

    def GET(self, idProducto):
        try:
            producto = PRODUCTO.detalleProductos(idProducto)
            return render.actualizar_productos(producto)
        except Exception as error:
            print(f'Ocurrió un error {error} - 105 | Controlador')
            return "Ocurrió un error"

    def POST(self, idProducto):
        try:
            entrada = web.input()
            producto =  {
                "producto": entrada.producto,
                "nombre":entrada.nombre_producto,
                "descripcion":entrada.descripcion,
                "precio":entrada.precio,
                "existencia":entrada.existencia
            }
            print(producto)
            if entrada and idProducto == entrada.producto:
                resultado = PRODUCTO.actualizarProductos(producto)
            if resultado:
                raise web.seeother("/")
        except Exception as error:
            print(f'Ocurrió un error {error} - 105_2 | Controlador')
            return "Oucrrió un error"