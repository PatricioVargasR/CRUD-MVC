import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()

render = web.template.render('mvc/views/', base='layout')

class ListaProductos:
    def GET(self):
        try:
            productos = PRODUCTO.listaProductos()
            print(productos)
            return render.lista_productos(productos)
        except Exception as error:
            return f"Ocurrió un error {error} - 101 | Crontolador"
