from django import forms

class Cityform(forms.Form):
    city_name = forms.CharField(label='City', max_length=30)
