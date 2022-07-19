
 
from django import forms

from .models import *



class MyCreateForm(forms.Form):

    name = forms.CharField()
    text = forms.CharField()
    age= forms.IntegerField()


    def clean_age(self):

        
        data= self.cleaned_data["age"]
        if data >200:
            raise forms.ValidationError("Tooooooooooo  old")
        return data

    def clean(self):
        cleaned_data=super().clean()

        name = self.cleaned_data["name"]
        text = self.cleaned_data["text"]
        if name in text:
            raise forms.ValidationError(" Name and Text must be different")
        


class SecondForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'
    
    
    def clean_year(self):

        
        data= self.cleaned_data["year"]
        if data <1999:
            raise forms.ValidationError(" car Tooooooooooo  old")
        return data

    def clean(self):
        cleaned_data=super().clean()

        reg = self.cleaned_data["reg"]
        price = self.cleaned_data["price"]
        
        if str(price) == reg:
            raise forms.ValidationError(" Name and Text must be different")
        
         
        
        


