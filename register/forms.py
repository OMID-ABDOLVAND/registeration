from django import forms

class EmailPhoneForm(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
