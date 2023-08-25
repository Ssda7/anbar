from django.urls import path

from . import views
from .views import ord_view

urlpatterns = [

    path("Order/", views.ord_view, name = "Order")
]