import web

render = web.template.render('mvc/views', base='layout')

class Creditos:

    def GET(self):
        try:
            return render.creditos()
        except Exception as error:
            print(f'Ocurrió un error {error} - 102 | Controlador')
            return "Ocurrió un error"