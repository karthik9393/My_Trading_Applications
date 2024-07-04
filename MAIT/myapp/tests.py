from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Order

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create(name="Test User", email="test@example.com")

def test_create_order(api_client, user):
    url = reverse('order-list')
    data = {
        "stock_symbol": "AAPL",
        "quantity": 10,
        "price": 150.00,
        "order_type": "limit",
        "time_in_force": "day",
        "user": user.user_id,
        "side": "buy"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Order.objects.count() == 1
    assert Order.objects.get().stock_symbol == "AAPL"

def test_order_status(api_client, user):
    order = Order.objects.create(
        user=user,
        stock_symbol="AAPL",
        quantity=10,
        price=150.00,
        order_type="limit",
        time_in_force="day",
        status="submitted"
    )
    url = reverse('order-detail', args=[order.order_id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['status'] == "submitted"
