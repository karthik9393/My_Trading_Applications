# mytradingapp/trading/views.py

from django.shortcuts import render, redirect, HttpResponse
from .forms import TradingForm

def create_trade_order(request):
    if request.method == 'POST':
        form = TradingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Ensure you have a URL named 'success_url'
    else:
        form = TradingForm()
    return render(request, 'trading/order_form.html', {'form': form})

def trade_success(request):
    return HttpResponse("Trade successfully processed!")  # Ensure this view if you want a success page
