from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('test', views.main_dashboard, name='main_dashboard'),
]
