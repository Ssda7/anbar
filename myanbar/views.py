from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Order

# Create your views here.





def Order(request):
    if request.method == 'POST':
        print(request.POST)
        sefaresh = Order.objects.all()



        total = ((request.POST.get("coffee_n")) * 5) + (request.POST.get("tea_n") * 3) + ((request.POST.get("cr_n") + request.POST.get("cake_n")) * 7)

        context = {
            'total':total
        }
        return render(request,'myanbar/total.html',context)
    else:
        context = [

        ]
        return render(request,'myanbar/Order.html',context)