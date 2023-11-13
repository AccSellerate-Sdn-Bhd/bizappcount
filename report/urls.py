from django.urls import path
from . import views

urlpatterns = [
    path('profit-and-loss', views.pandlreports, name='profit_and_loss'),
    path('balance-sheet', views.balancesheetreports, name='balance_sheet'),
    path('cash-flow', views.cashflowreports, name='cash_flow'),
    path('run-trial-balance', views.runtrialbalancereports, name='run_trial_balance'),
    path('general-ledger', views.generalledgerreports, name='general_ledger'),
    path('inventory-report', views.inventoryreports, name='inventory_report'),

    path('convert_to_ledger/<str:url>/', views.convertToLedger, name='convert_to_ledger'),

    path('generate_profit_and_loss', views.generate_profit_and_loss_report, name='generate_pdf_report'),
    path('generate_balance_sheet', views.generate_balance_sheet_report, name='generate_pdf_report'),
    path('generate_cash_flow', views.generate_cash_flow_report, name='generate_pdf_report'),
    path('generate_run_trial_balance', views.generate_run_trial_balance, name='generate_pdf_report'),
    path('generate_general_ledger', views.generate_general_ledger_reports, name='generate_pdf_report'),
    path('generate_inventory_report', views.generate_inventory_reports, name='generate_pdf_report'),
]
