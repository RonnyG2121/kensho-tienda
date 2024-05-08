# formulario de contacto

from django import forms

# Creando el formulario
class Formcontacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=50)
    apellido = forms.CharField(label='Apellido', required=True, max_length=50)
    email = forms.EmailField(label='Correo Electrónico', required=True)
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea)
