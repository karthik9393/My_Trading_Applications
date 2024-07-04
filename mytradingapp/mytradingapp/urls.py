# mytradingapp/mytradingapp/urls.py

from django.urls import path
from trading import views  # Make sure this import is correct

urlpatterns = [
    path('trade/', views.create_trade_order, name='trade_order'),
    path('trade/success/', views.trade_success, name='success_url'),  # Ensure this path if you implemented a success view
]
