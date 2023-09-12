from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    Item_name = models.CharField(max_length=200)
    tedad = models.IntegerField(default=0)
    prov_name = models.CharField(max_length=200)
    
    class shomare(models.IntegerChoices):
        YEK = 1
        DO = 2
        SE = 3

    shomare_anbar = models.IntegerField(choices = shomare.choices)

    def __str__(self):
        return self.Item_name
    
class Sefaresh(models.Model):
    name = models.CharField(max_length=200)
    table = models.IntegerField(default=0)
    date = models.DateTimeField("date published")
    desired_time = models.DateTimeField("desired date")
    coffee_n = models.IntegerField(default=0)
    tea_n = models.IntegerField(default=0)
    cr_n = models.IntegerField(default=0)
    cake_n = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PromoCode(models.Model):
    p_code = models.CharField(max_length=200, unique=True)
    discount = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    time_used = models.IntegerField(default=0)
    def __str__(self):
        return self.p_code


    