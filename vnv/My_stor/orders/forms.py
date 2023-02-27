from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Type here'})
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Type here'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Type here'})
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Type here'})
    )
    postal_code = forms.CharField(
        label='Postal Code',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Type here'})
    )
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Type here'})
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
