from django import forms
# from product import Product
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.Form):
    class Meta:
        model = Product
        fields = ["name"]
        widgets = {
            'name': forms.SearchForm(attrs={'class': 'form-control'}),
            'placeholder': _('Product'),
        }
