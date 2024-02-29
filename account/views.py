from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get('email')
            username = request.POST.get('username')
            user = User.objects.filter(email__iexact=user_email,username__iexact=username).exists()
            if not user:
                user_pass = request.POST.get('password')
                new_user = User(email=user_email, email_active_code=get_random_string(80),username=username)
                new_user.is_active = False
                new_user.set_password(user_pass)
                # TODO: send activate code to user email
                new_user.save()
                # TODO: send message with this redirect
                return redirect(reverse('account:login_page'))
            else:
                form.add_error('username','این نام کاربری ثبت شده')
                form.add_error('email', 'این ایمیل قبلا ثبت نام کرده است')
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': RegisterForm})

def login_page(request):
    if request.method == "POST":
        pass
    return render(request, 'login.html', {'form':LoginForm})



def activate_account(request, activate_code):
    user = User.objects.filter(email_active_code__iexact=activate_code).first()
    if user:
        user.is_active = True
        user.email_active_code = get_random_string(80)
        user.save()
        return redirect(reverse('account:login_page'))
    else:
        return redirect(reverse('account:register'))