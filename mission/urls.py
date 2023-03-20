from django.urls import path
from django.urls import reverse_lazy
from . import views

app_name = 'mission'

urlpatterns = [
    path('', views.mission_list, name='mission_list'),
    path('<int:id>/<slug:slug>/', views.mission_detail, name='mission_detail'),
]