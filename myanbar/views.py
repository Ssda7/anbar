from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .models import Order, PromoCode, Item, ItemOrder
from django.utils import timezone

# Create your views here.





def ord_view(request):

    items = Item.objects.all().exclude(amount=0)
    if request.method == 'POST':
        print(request.POST)


        c_name = request.POST.get("name")
        order_date = timezone.now()
        des_time = request.POST.get("desiredtime")
        table_n = int(request.POST.get("table"))

        #Create a new Order Instance:
        order = Order.objects.create(name = c_name, date = order_date, desired_time = des_time, table = table_n)


        total_price = 0

        for item in items:
            quantity = int(request.POST.get('quantity_' + str(item.id)))
            i_name = str(request.POST.get('item_name_' + str(item.id)))
            specific_item = Item.objects.get(item_name = i_name)
            if quantity > specific_item.amount:
                return redirect("http://127.0.0.1:8000/Bar/Order/")
                break
            
            specific_item.amount -= quantity
            specific_item.save()
            order.itemorder_set.create(item = specific_item, quantity = quantity)

            total_price += specific_item.price * quantity
                


 
        user_code = request.POST.get("promo")
        try:
            d = PromoCode.objects.get(p_code = user_code)
            d.time_used += 1
            disc = d.discount
            d.save()
            total_price -= disc
            order.cost = total_price
            order.promo_used = d
            order.save()
            
        except: 
            disc = 0
            total_price -= disc
            order.cost = total_price
            order.save()

        context = {
            'total':total_price,
            'c_name':c_name,
            'order_date':order_date,
            'des_time':des_time,
            'table':table_n,
            
        }

        return render(request,'myanbar/total.html',context)
    else:
        context = {
            'items': items

        }
        return render(request,'myanbar/Order.html',context)
    