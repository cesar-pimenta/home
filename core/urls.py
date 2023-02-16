from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('list', views.post_list, name='post_list'),
    path('list/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('list/<int:post_id>/share/', views.post_share, name='post_share'),
]
