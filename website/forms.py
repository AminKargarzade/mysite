from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=255)
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)