from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inventory'),
    path('create', views.create, name='create_nventory'),
    path('edit/<int:id>', views.edit, name='edit_inventory'),
    path('history/<int:id>', views.history, name='history_inventory'),
    path('api/delete/<int:id>', views.delete, name='api_delete_inventory'),
]
