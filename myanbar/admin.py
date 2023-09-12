from django.contrib import admin

from .models import Item, Sefaresh, PromoCode

# Register your models here.

admin.site.register(Item)
admin.site.register(Sefaresh)
admin.site.register(PromoCode)