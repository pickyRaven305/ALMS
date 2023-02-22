from django import forms 
from .models import Item
from django.contrib.auth.models import User

category=(
    ("food","FOOD"),
    ("clothing","CLOTHING"),
    ("utensils","UTENSILS"),
    ("books","BOOKS"),
    ("Others","OTHERS"),
)        
class AddItemForm(forms.Form):
    item_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Please enter the  Item Name'}))
    item_category = forms.ChoiceField(choices=category, required=False,widget=forms.RadioSelect())
    desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))
    cost = forms.IntegerField(min_value=1,required=False,widget=forms.TextInput(attrs={'placeholder': 'Please enter the  Item Cost'}))
    image = forms.ImageField(required = False)
    class Meta:
        model = Item
        fields="__all__"
        
class DonateForm(forms.Form):
    amount = forms.IntegerField(min_value=1,required=False,widget=forms.TextInput(attrs={'placeholder': 'Please enter the  donaated amount'}))