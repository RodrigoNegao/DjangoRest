from django import forms
from Foods.models import Food



class FoodsForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['foodName','price','pictureFood','description','is_published'] #'__all__'
