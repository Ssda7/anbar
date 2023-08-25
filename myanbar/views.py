from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Sefaresh
from django.utils import timezone

# Create your views here.





def ord_view(request):
    if request.method == 'POST':
        print(request.POST)
        sefaresh = Sefaresh.objects.all()


        c_name = request.POST.get("name")
        order_date = timezone.now()
        des_time = request.POST.get("desiredtime")
        table_n = int(request.POST.get("table"))
        tc = int(request.POST.get("Coffee_n"))
        tt = int(request.POST.get("Tea_n"))
        tcr = int(request.POST.get("Cr_n"))
        tca = int(request.POST.get("Cake_n"))
        total = (tc * 5) + (tt * 3) + (tcr + tca) * 7


        s = Sefaresh(name = c_name, date = order_date, desired_time = des_time, table = table_n, coffee_n = tc, tea_n = tt, cr_n = tcr, cake_n = tca, cost = total)
        s.save()

        context = {
            'total':total,
            'c_name':c_name,
            'order_date':order_date,
            'des_time':des_time,
            'table':table_n,
            'tc':tc,
            'tt':tt,
            'tcr':tcr,
            'tca':tca
        }

        return render(request,'myanbar/total.html',context)
    else:
        context = {

        }
        return render(request,'myanbar/Order.html',context)