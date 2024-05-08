
# Creando la clase carrito para hacer un carrito en el sitio web

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = { }
        self.carro = carro

    def Agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
            'producto_id': producto.id,
            'nombre': producto.nombre,
            'precio': str(producto.precio),
            'cantidad': 1,
            'imagen': producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1
                    value['precio'] = float(value['precio']) + producto.precio
                    break
        self.Guardar_carro()

    def Guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def Eliminar(self, producto):
        producto_id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.Guardar_carro()

    def Restar(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] -1
                    value['precio']=float(value['precio'])-producto.precio
                    if value['cantidad'] -1:
                        self.Eliminar(producto)
                    break
        self.Guardar_carro()
        if value['cantidad'] < 1:
            self.Eliminar(producto)

    def Limpiar_carro(self):
        self.carro = self.session["carro"] = { }
        self.session.modified = True

