from django.forms import ModelForm
from django import forms
from .models import ItemModel

class AddItemForm(ModelForm):

    class Meta:
        model = ItemModel
        fields = ['link','target_price','current_price','img']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].required = False