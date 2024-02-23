import web

render = web.template.render('mvc/views/', base='layout')

class BorrarProductos:

    def GET(self):
        try:
            return render.borrar_productos()
        except Exception as error:
            print(f'Ocurrió un error: {error} - 106 | Controlador')
            return "Ocurrió un error"
