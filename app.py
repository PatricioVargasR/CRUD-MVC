# Importamos el módulo correspondinete
import web

# Definimos las URLS y Controlaadores de nuestra paǵina
urls = (
    '/', 'mvc.controllers.lista_productos.ListaProductos',
    '/creditos', 'mvc.controllers.creditos.Creditos',
    '/detalle/(.*)', 'mvc.controllers.detalle_productos.DetalleProductos',
    '/insertar', 'mvc.controllers.insertar_productos.InsertarProductos',
    '/actualizar/(.*)', 'mvc.controllers.actualizar_productos.ActualizarProductos',
    '/borrar/(.*)', 'mvc.controllers.borrar_productos.BorrarProductos'
    )

# Creamos la aplicación con las URLS y las clases
app = web.application(urls, globals())

# Ejecutamos el código en caso de que este archivo sea el principal
if __name__ == '__main__':
    app.run()
