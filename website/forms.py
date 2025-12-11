from django import forms
from website.models import Contact

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=255)
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }