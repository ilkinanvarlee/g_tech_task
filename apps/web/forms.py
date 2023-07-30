from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    phone = forms.IntegerField()
    message = forms.CharField(max_length=50)
