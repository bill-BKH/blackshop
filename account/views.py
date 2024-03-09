from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def register(request):
    if not request.user.is_authenticated:
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
                    new_user.save()
                    messages.success(request,"به حساب خود ورود کنید")
                    return redirect('account:login_page')
                else:
                    form.add_error('username','این نام کاربری ثبت شده')
                    form.add_error('email', 'این ایمیل قبلا ثبت نام کرده است')
                    return render(request, 'register.html', {'form': form})
            else:
                return render(request, 'register.html', {'form': form})
        return render(request, 'register.html', {'form': RegisterForm})
    else:
        return redirect(reverse('shop:index'))

def login_page(request):
    if request.method == "POST":
        user_email = request.POST.get('email')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email__iexact=user_email).first()
            if user:
                if user.is_active == True:
                    user_pass = request.POST.get('password')
                    password_is_correct = user.check_password(user_pass)
                    if password_is_correct:
                        login(request, user)
                        return redirect(reverse('shop:index'))
                    else:
                        form.add_error('email', 'ایمیل یا پسورد شما اشتباه است')
                        return render(request, 'login.html', {'form':form})
        else:
            form.add_error('email', 'ایمیل یا پسورد شما اشتباه است')
            return render(request, 'login.html', {'form':form})
            
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



def logout_page(request):
    logout(request)
    return redirect(reverse('account:login_page'))
