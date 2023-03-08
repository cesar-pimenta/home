from django.urls import path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    path('', views.store_root, name='store_root'),
]