from django.urls import path
from . import views

urlpatterns = [
    path('trade/', views.trade_view, name='trade'),
]
