from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_dashboard, name='expenses_dashboard'),
    path('create/', views.create_expenses, name='create_expense'),
    path('delete/<str:expense_id>/',  views.delete_expenses, name='delete_expenses'),
    path('delete_expenses_line/<str:expenses_line_id>/',  views.delete_expenses_line, name='delete_expenses_line'),
    path('edit_expenses/<str:expenses_id>/', views.edit_expenses, name='edit_expenses'),
    path('generate_purchase_order/<str:expenses_id>/', views.generate_purchase_order, name='generate_purchase_order'),
    #path('edit_expenses_line/<str:expenses_line_id>/', views.edit_expenses_line, name='edit_expenses_line'),
    path('api/create_expense/', views.create_expense_api, name='create_expense_api'),
    path('upload_receipt/', views.upload_receipt, name='upload_receipt'),
    path('upload_do/', views.upload_do, name='upload_do'),
    #path('upload_receipt/<int:expenses_id>/', views.upload_receipt, name='upload_receipt'),
    #path('upload_do/<int:expenses_id>/', views.upload_do, name='upload_do'),
]
