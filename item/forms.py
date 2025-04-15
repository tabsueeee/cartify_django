from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']

        widgets = {
            'category': forms.Select(attrs={'class': 'w-full py-2 px-4'}),
            'name': forms.TextInput(attrs={'class': 'w-full py-2 px-4', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-2 px-4', 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-2 px-4', 'placeholder': 'Price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full py-2 px-4'}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'w-full py-2 px-4', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(
                attrs={'class': 'w-full py-2 px-4', 'placeholder': 'Description'}),
            'price': forms.NumberInput(
                attrs={'class': 'w-full py-2 px-4', 'placeholder': 'Price'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'w-full py-2 px-4'}),
        }