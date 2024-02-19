import web

render = web.template.render('mvc/views/', base='layout')

class ActualizarProductos:

    def GET(self):
        try:
            return render.actualizar_productos()
        except Exception as error:
            return f'Ocurrió un error {error} - 105 | Controlador'