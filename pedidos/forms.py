
from django import forms


class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Número de la tarjeta', required=True)
    exp_month = forms.IntegerField(label='Mes de expiración', required=True)
    exp_year = forms.IntegerField(label='año de expiración', required=True)
    cvc = forms.CharField(
        label='Código seguro de verificación(CVC)', required=True)
