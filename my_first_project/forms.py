from django import forms

class Contact_form(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(label="Enter Your Email")
    feedback = forms.CharField(widget=forms.Textarea)