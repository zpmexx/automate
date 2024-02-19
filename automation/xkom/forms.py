from django.forms import ModelForm
from django import forms
from .models import ItemModel

class AddItemForm(ModelForm):

    class Meta:
        model = ItemModel
        fields = ['name','link','target_price','current_price','img']