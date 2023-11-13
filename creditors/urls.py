from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='creditors'),
    path('create', views.create, name="creditors_create"),
    path('edit/<str:id>', views.edit, name='edit_creditor'),
    path('api/delete/<str:id>', views.delete, name='api_delete_creditor'),
]
