from django import forms

from applications.core.models import JoinUs


class JoinUsForm(forms.ModelForm):
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'placeholder': '+996(xxx)xx-xx-xx'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'placeholder': 'Ваш адрес'}))

    class Meta:
        model = JoinUs
        fields = ('form_type', 'name', 'phone', 'address', 'ownership')
