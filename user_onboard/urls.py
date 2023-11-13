from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/user/1', views.onboard_1, name='onboard_1'),
    path('register/user/2', views.onboard_2, name='onboard_2'),
    path('register/user/3', views.onboard_3, name='onboard_3'),
    path('dashboard/account-setup', views.onboard_4, name='onboard_4'),
    
    path('dashboard/bank/create', views.create_bank, name='create_bank'),
    path('dashboard/bank/edit/<int:id>', views.edit_bank, name='edit_bank'),
    path('api/bank/delete/<int:id>', views.delete_bank, name="delete_bank"),

    path('dashboard/office/create', views.create_office, name='create_office'),
    path('dashboard/office/edit/<int:id>', views.edit_office, name='edit_office'),
    path('api/office/delete/<int:id>', views.delete_office, name="delete_office"),

    path('dashboard/staff/create', views.create_staff, name='create_staff'),
    path('dashboard/staff/edit/<int:id>', views.edit_staff, name='edit_staff'),
    path('api/staff/delete/<int:id>', views.delete_staff, name="delete_staff"),

    path('dashboard/product/create', views.create_product, name='create_product'),
    path('dashboard/product/edit/<int:id>', views.edit_product, name='edit_product'),
    path('api/product/delete/<int:id>', views.delete_product, name="delete_product"),

    path('dashboard/loan/create', views.create_loan, name='create_loan'),
    path('dashboard/loan/edit/<int:id>', views.edit_loan, name='edit_loan'),
    path('api/loan/delete/<int:id>', views.delete_loan, name="delete_loan"),

    path('dashboard/software-cost/create', views.create_software_cost, name='create_software_cost'),
    path('dashboard/software-cost/edit/<int:id>', views.edit_software_cost, name='edit_software_cost'),
    path('api/software-cost/delete/<int:id>', views.delete_software_cost, name="delete_software_cost"),


    path('dashboard/owner-equity/create', views.create_owner_equity, name='create_owner_equity'),
    path('dashboard/owner-equity/edit/<int:id>', views.edit_owner_equity, name='edit_owner_equity'),
    path('api/owner-equity/delete/<int:id>', views.delete_owner_equity, name="delete_owner_equity"),
]
