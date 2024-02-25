import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()

render = web.template.render('mvc/views/', base='layout')

class ListaProductos:
    def GET(self):
        try:
            productos = PRODUCTO.listaProductos()
            return render.lista_productos(productos)
        except Exception as error:
            print(f"Ocurrió un error {error} - 101 | Controlador")
            return "Ocurrió un error"

    def POST(self):
        try:
            entrada = web.input()
            producto_buscado = entrada.nombre
            print(producto_buscado)
            if entrada and producto_buscado:
                respuesta = PRODUCTO.buscarProductos(producto_buscado)
            if respuesta:
                return render.lista_productos(respuesta)
            else:
                raise web.seeother("/")
        except Exception as error:
            print(f"Ocurrió un error {error} - 101_2 | Controlador")
            return "Ocurrió un error"