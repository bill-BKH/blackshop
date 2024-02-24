from django import forms
from .models import Contact
class ContactForm(forms.Form):
    name = forms.CharField(
        label='نام و نام خانوادگی',
        widget=forms.TextInput(attrs={
            'class':'test'
        })
    )
    email = forms.EmailField()
    message = forms.CharField()

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'message': 'پیام شما'
        }
        widgets = {
            'name': forms.TextInput(attrs={
            'class':'test'
        }),
            'email':forms.TextInput(attrs={
            'class':'test'
        })
        }