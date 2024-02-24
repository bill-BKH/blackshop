from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
        attrs={
            'class': 'input-ui pr-2',
            'placeholder': 'ایمیل خود را وارد کنید'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())


    def clean_password_confirm(self):
        password = self.cleaned_data["password"]
        password_confirm = self.cleaned_data["password_confirm"]
        if password == password_confirm:
            return password_confirm
        else:
            raise ValidationError('پسورد با تکرار آن مطابقت ندارد')