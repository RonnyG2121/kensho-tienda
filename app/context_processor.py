from datetime import datetime


def RetornaAnio(request):
    return {'year': datetime.now().year}
