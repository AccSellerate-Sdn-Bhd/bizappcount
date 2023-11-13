from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='account'),
    path('create', views.create, name="account_create")
]
