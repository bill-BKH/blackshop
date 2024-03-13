from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('',views.product, name = "product"),
    path('single-page/<slug:slug>',views.single, name='single')
]