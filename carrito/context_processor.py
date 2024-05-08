# Creando el context?processor para el carrito de compras
def Importe_total_carro(request):
    total = 0
    if request.user.is_authenticated and request.session.__contains__('carro'):
        for key, value in request.session["carro"].items():
            total += float(value["precio"])
        return {"importe_total_carro": total}
    else:
        total = "Debes registrarte para poder agregar productos al carro y comprar"
        return {"importe_total_carro": total}
