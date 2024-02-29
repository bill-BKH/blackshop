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
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(
            attrs = {
            'class': 'input-ui pr-2',
            'placeholder': 'نام کاربری خود را وارد کنید'
            }
        )
    )
    password = forms.CharField(
        label ='پسورد خود را وارد کنید',
        widget=forms.PasswordInput(
        attrs={
            'class': 'input-ui pr-2',
            'placeholder': 'پسورد خود را وارد کنید'
        }
    ))
    
    password_confirm =  forms.CharField(
        label ='پسورد خود را وارد کنید',
        widget=forms.PasswordInput(
        attrs={
            'class': 'input-ui pr-2',
            'placeholder': 'پسورد خود را وارد کنید'
        }
    ))
    

    def clean_password_confirm(self):
        password = self.cleaned_data["password"]
        password_confirm = self.cleaned_data["password_confirm"]
        if password == password_confirm:
            return password_confirm
        else:
            raise ValidationError('پسورد با تکرار آن مطابقت ندارد')
        



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
        attrs={
            'class': 'input-ui pr-2',
            'placeholder': 'ایمیل خود را وارد کنید'
        }
    ))
    password = forms.CharField(
        label ='پسورد خود را وارد کنید',
        widget=forms.PasswordInput(
        attrs={
            'class': 'input-ui pr-2',
            'placeholder': 'پسورد خود را وارد کنید'
        }
    ))
    