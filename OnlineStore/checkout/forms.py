from django import forms

from .models import Order


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class OrderCreateForm(PlaceholderForm):
    first_name = forms.CharField(max_length=100, help_text='Имя')
    last_name = forms.CharField(max_length=100, help_text='Фамилия')
    email = forms.EmailField(help_text='Email')
    phone = forms.CharField(max_length=20, help_text='Телефон')
    address_line_1 = forms.CharField(max_length=100, help_text='Адрес')
    address_line_2 = forms.CharField(
        max_length=100,
        required=False,
        help_text='Адрес (дополнительно)'
    )
    payment_method = forms.ChoiceField(choices=Order.PAYMENT_METHOD_CHOICES)
