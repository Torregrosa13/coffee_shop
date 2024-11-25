from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    desc = forms.CharField(max_length=300, label="Descripcion")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    image = forms.ImageField(label="Imagen", required=False)

    def save(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            desc = self.cleaned_data['desc'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            image = self.cleaned_data['image']
        )