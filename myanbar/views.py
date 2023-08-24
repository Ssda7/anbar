from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.



def index(request):
    return HttpResponse("Salam, etelaate Iteme morede nazar ra vared konid.")

def home(request):
    if request.method == 'POST':
        sefaresh = Order.objects.all()
        total = (Order.coffee_n * 5) + (Order.tea_n * 3) + ((Order.cr_n + Order.cake_n) * 7)
        context = {
            'total':total
        }
        return render(request,'Bar/total.html',context)
    else:
        context = [

        ]
        return render(request,'Bar/Order.html',context)