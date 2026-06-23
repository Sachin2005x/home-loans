from django.urls import path
from .views import *

urlpatterns = [

    # Home
    path('', home, name='home'),

    # About
    path('about/', about, name='about'),

    # Services Overview
    path('services/', services, name='services'),

    # Individual Services
    path('services/home-purchase/', home_purchase, name='home_purchase'),
    path('services/construction/', construction, name='construction'),
    path('services/renovation/', renovation, name='renovation'),
    path('services/lap/', loan_against_property, name='lap'),
    path('services/extension/', extension, name='extension'),
    path('services/plot-construction/', plot_construction, name='plot_construction'),
    path('services/balance-transfer/', balance_transfer, name='balance_transfer'),
    path('services/topup/', topup, name='topup'),

    # Calculators
    path('emi-calculator/', emi_calculator, name='emi_calculator'),

    # Interest Rates (removed)

    # (removed Malayalam page)

    # Success Pages
    path('success/', success, name='success'),
    path('callback-success/', callback_success, name='callback_success'),
]
