from django import forms
from .models import *




class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control',
                                            'onchange': 'loadFile(event)'
            }
            ),
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "amount": forms.NumberInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "activate": forms.CheckboxInput(attrs={'checked':False}),
            "shop": forms.Select(attrs={'class': 'form-control'}),

        }
        images = forms.ModelMultipleChoiceField(
            queryset=Shop.objects.all(),
            widget=forms.CheckboxSelectMultiple()
        )

