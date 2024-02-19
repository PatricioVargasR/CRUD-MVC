import web

render = web.template.render('mvc/views/', base='layout')

class InsertarProductos:

    def GET(self):
        try:
            return render.insertar_productos()
        except Exception as error:
            return f'Ocurrió un error {error} - 104 | Controlador'