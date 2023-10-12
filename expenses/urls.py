from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_dashboard, name='expenses_dashboard'),
    path('create/', views.create_expenses, name='create_expense'),
    path('delete/<str:expense_id>/',  views.delete_expenses, name='delete_expenses'),
    path('delete_expenses_line/<str:expenses_line_id>/',  views.delete_expenses_line, name='delete_expenses_line'),
    path('edit_expenses/<str:expenses_id>/', views.edit_expenses, name='edit_expenses'),
    #path('edit_expenses_line/<str:expenses_line_id>/', views.edit_expenses_line, name='edit_expenses_line'),
    path('api/create_expense/', views.create_expense_api, name='create_expense_api'),
]
