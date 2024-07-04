from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Account, Order, Execution, MarketData, ReferenceData
from .serializers import UserSerializer, AccountSerializer, OrderSerializer, ExecutionSerializer, MarketDataSerializer, ReferenceDataSerializer
from .services import TradingService
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = User.objects.get(user_id=request.data['user'])
        stock_symbol = request.data['stock_symbol']
        quantity = request.data['quantity']
        price = request.data['price']
        order_type = request.data['order_type']
        time_in_force = request.data['time_in_force']
        side = request.data['side']  # 'buy' or 'sell'

        new_order = TradingService.create_order(user, stock_symbol, quantity, price, order_type, time_in_force, side)

        if new_order:
            serializer = self.get_serializer(new_order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Order creation failed"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        status = TradingService.fetch_order_status(order.order_id)
        data = self.get_serializer(order).data
        data['status'] = status
        return Response(data)

class ExecutionViewSet(viewsets.ModelViewSet):
    queryset = Execution.objects.all()
    serializer_class = ExecutionSerializer
    permission_classes = [IsAuthenticated]

class MarketDataViewSet(viewsets.ModelViewSet):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        stock_symbol = request.query_params.get('stock_symbol')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date', timezone.now().date().isoformat())
        data = TradingService.fetch_market_data(stock_symbol, start_date, end_date)
        if data is not None:
            return Response(data.to_dict())
        else:
            return Response({"error": "Market data fetching failed"}, status=status.HTTP_400_BAD_REQUEST)

class ReferenceDataViewSet(viewsets.ModelViewSet):
    queryset = ReferenceData.objects.all()
    serializer_class = ReferenceDataSerializer
    permission_classes = [IsAuthenticated]
