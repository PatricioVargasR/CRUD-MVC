import web

urls = (
    '/', 'mvc.controllers.lista_productos.ListaProductos',
    '/creditos', 'mvc.controllers.creditos.Creditos',
    '/detalle/(.*)', 'mvc.controllers.detalle_productos.DetalleProductos',
    '/insertar', 'mvc.controllers.insertar_productos.InsertarProductos',
    '/actualizar/(.*)', 'mvc.controllers.actualizar_productos.ActualizarProductos',
    '/borrar/(.*)', 'mvc.controllers.borrar_productos.BorrarProductos'
    )

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
