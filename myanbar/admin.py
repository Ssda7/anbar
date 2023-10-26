from django.contrib import admin

from .models import Item, Order, PromoCode, ItemOrder

# Register your models here.

class ItemSet(admin.TabularInline):
    model = ItemOrder
    extra = 3
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Order Information', {
            'fields': ('name', 'table', 'date', 'desired_time', 'cost', 'promo_used')
        }),
        #('Advanced Options', {
        #    'classes': ('collapse',),
        #    'fields': ('order_id',),
        #}),
    )
    inlines = [ItemSet]
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
admin.site.register(PromoCode)