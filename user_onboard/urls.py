from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/user/1', views.onboard_1, name='onboard_1'),
    path('register/user/2', views.onboard_2, name='onboard_2'),
    path('register/user/3', views.onboard_3, name='onboard_3'),
    path('dashboard/account-setup', views.onboard_4, name='onboard_4'),
    path('dashboard/bank/create', views.create_bank, name='create_bank'),
    path('dashboard/office/create', views.create_office, name='create_office'),
    path('dashboard/staff/create', views.create_staff, name='create_staff'),
    path('dashboard/product/create', views.create_product, name='create_product'),
    path('dashboard/loan/create', views.create_loan, name='create_loan'),
    path('dashboard/software-cost/create', views.create_software_cost, name='create_software_cost'),
    path('dashboard/owner-equity/create', views.create_owner_equity, name='create_owner_equity'),
]
