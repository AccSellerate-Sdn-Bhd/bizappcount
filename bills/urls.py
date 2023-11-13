from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bills'),
    path('create', views.create, name="bills_create"),
    path('edit/<int:id>', views.edit, name='edit_bill'),
    path('api/delete/<int:id>', views.delete, name='api_delete_bill'),
]
