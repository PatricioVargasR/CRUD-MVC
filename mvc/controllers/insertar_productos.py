import web

render = web.template.render('mvc/views/', base='layout')

class InsertarProductos:

    def GET(self):
        try:
            return render.insertar_productos()
        except Exception as error:
            print(f'Ocurrió un error {error} - 104 | Controlador')
            return "Ocurrió un error"
