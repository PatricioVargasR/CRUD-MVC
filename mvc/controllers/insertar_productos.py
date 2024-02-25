import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()

render = web.template.render('mvc/views/', base='layout')

class InsertarProductos:

    def GET(self):
        try:
            return render.insertar_productos()
        except Exception as error:
            print(f'Ocurrió un error: {error} - 104 | Controlador')
            return "Ocurrió un error"

    def POST(self):
        try:
            entrada = web.input()
            producto =  {
                "nombre":entrada.nombre_producto,
                "descripcion":entrada.descripcion,
                "precio":entrada.precio,
                "existencia":entrada.existencia
            }
            print(producto)
            if entrada:
                resultado = PRODUCTO.insertarProductos(producto)
            if resultado:
                raise web.seeother("/")
        except Exception as error:
            print(f"Ocurrió un error: {error} - 104_2 | Controlador")
            return "Ocurrió un error"