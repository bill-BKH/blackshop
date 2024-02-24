from django.shortcuts import render
from .models import User
from .forms import RegisterForm
from django.http import HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_email = request.POST.get('email')
            user = User.objects.filter(email__iexact=user_email).exists()
            if not user:
                user_pass = request.POST.get('password')

                new_user = User(email=user_email, email_active_code=get_random_string(80), username=user_email)
                new_user.set_password(user_pass)
                new_user.save()
            else:
                form.add_error('email', 'این ایمیل قبلا ثبت نام کرده است')
                return render(request, 'register.html', {'form': form})


        else:
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': RegisterForm})
