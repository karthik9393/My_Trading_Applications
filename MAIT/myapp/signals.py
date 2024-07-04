from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def execute_order(sender, instance, **kwargs):
    # Business logic after an order is saved
    pass
