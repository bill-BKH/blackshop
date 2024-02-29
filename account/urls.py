from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('activate-account/<str:activate_code>', views.activate_account)
]