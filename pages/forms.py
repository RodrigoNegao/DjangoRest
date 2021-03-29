from django import forms
from Foods.models import Food



class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['employer','foodName','price','pictureFood','description','is_published'] #'__all__'
