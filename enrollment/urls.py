from django.urls import path
from . import views

app_name = 'enrollment'

urlpatterns = [
    path('<int:id>/<slug:slug>/', views.main, name='enrollment_main'),
]