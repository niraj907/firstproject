from django import forms

class contactForms(forms.Form):
    name = forms.CharField(label = "name")
    email = forms.EmailField(label = "email")
    message = forms.CharField(widget=forms.Textarea)