import web

render = web.template.render('mvc/views/', base='layout')

class DetalleProductos:

    def GET(self):
        try:
            return render.detalle_productos()
        except Exception as error:
            print(f'Ocurrió un error {error} - 103 | Controlador')
            return "Ocurrió un error"
