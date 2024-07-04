from django.contrib import admin
from .models import User, Account, Order, Execution, MarketData, ReferenceData

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Order)
admin.site.register(Execution)
admin.site.register(MarketData)
admin.site.register(ReferenceData)
