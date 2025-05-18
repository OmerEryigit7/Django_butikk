from .models import ProductInfo
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = ['name', 'price', 'description', 'stock', 'image']
        labels = {
            'name': 'Navn',
            'price': 'Pris',
            'description': 'Beskrivelse',
            'stock': 'Antall på lager',
            'image': 'Bilde'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Navn på produkt'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Bare tall'}),
            'description': forms.Textarea( attrs={'placeholder': 'Gi en kort beskrivelse av produktet'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Antall'}),
        }

