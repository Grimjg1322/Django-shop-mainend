from django import forms

ORDER_TYPE = {
    ('S', 'Самовывоз'),
    ('D', 'Доставка'),
}
PAYMENT = {
    ('C', 'Карта'),
    ('Q', 'Qiwi'),
}
class CheckoutForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Pavel',
        'class': 'form-control',
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Leletko',
        'class': 'form-control',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+7 (910) 123 4567',
        'class': 'form-control',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'г.Брянск',
        'class': 'form-control',
    }))
    telegram = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
    }), required=False)
    payment = forms.ChoiceField(choices=ORDER_TYPE)