from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_dashboard, name='sales_dashboard'),
    path('create/', views.create_sales, name='create_sales'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('get_customer_data/<int:customer_id>/', views.get_customer_data, name='get_customer_data'),
    path('generate_quotation/<str:sales_id>/', views.generate_quotation, name='generate_quotation'),
    path('generate_invoice/<str:sales_id>/', views.generate_invoice, name='generate_invoice'),
    path('generate_do/<str:sales_id>/', views.generate_do, name='generate_do'),
    path('generate_receipt/<str:sales_id>/', views.generate_receipt, name='generate_receipt'),
    path('api/sales/create/', views.create_sales_api, name='api_create_sales'),
    path('api/customer/add/', views.add_customer_api, name='api_add_customer'),
    path('delete/<str:sales_id>/',  views.delete_sales, name='delete_sales'),
    path('delete_sales_line/<str:sales_line_id>/',  views.delete_sales_line, name='delete_sales_line'),
    path('edit_sales/<str:sales_id>/', views.edit_sales, name='edit_sales'),
    path('edit_sales_line/<str:sales_line_id>/', views.edit_sales_line, name='edit_sales_line'),

]
