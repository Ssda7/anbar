from django.urls import path

from . import views
from .views import Order

urlpatterns = [

    path("Order/", views.Order, name = "Order")
]