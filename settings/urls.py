from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.customer_dashboard, name='customer_dashboard'),
    path('customer/create', views.create_customer, name='create_customer'),
    path('customer/delete//<str:customer_id>/', views.delete_customer, name='delete_customer'),
     path('customer/edit/<str:customer_id>/', views.edit_customer, name='edit_customer'),

]
