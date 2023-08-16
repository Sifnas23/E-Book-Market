from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('Name', 'Book_Name', 'Description', 'price', 'Image')

        widgets = {
            'Name': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'Book_Name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('Book_Name', 'Description', 'price', 'Image', 'is_sold')
        widgets = {
            'Book_Name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }



