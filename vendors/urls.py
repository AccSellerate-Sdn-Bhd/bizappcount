from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='vendors'),
    path('create', views.create, name="vendors_create"),
    path('edit/<str:id>', views.edit, name='edit_vendor'),
    path('api/delete/<str:id>', views.delete, name='api_delete_vendor'),
]
