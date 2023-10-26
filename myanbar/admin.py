from django.contrib import admin

from .models import Item, Order, PromoCode, ItemOrder

# Register your models here.

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(PromoCode)
admin.site.register(ItemOrder)