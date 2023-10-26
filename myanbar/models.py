from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    amount = models.PositiveIntegerField(default=0)
    prov_name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    
    class number(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
    shomare_anbar = models.IntegerField(choices = number.choices)

    def __str__(self):
        return self.item_name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    table = models.IntegerField(default=0)
    date = models.DateTimeField("date published")
    desired_time = models.DateTimeField("desired date")
    cost = models.IntegerField(default=0)
    promo_used = models.ForeignKey("PromoCode", on_delete=models.PROTECT, default=None, blank=True, null=True)


    def __str__(self):
        return self.name
    
class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} of {self.item} item in {self.order}'s order"

class PromoCode(models.Model):
    p_code = models.CharField(max_length=200, unique=True, primary_key=True)
    discount = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    time_used = models.IntegerField(default=0)
    def __str__(self):
        return self.p_code


    