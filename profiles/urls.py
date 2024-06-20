from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'), # This is the route URL 
    path('order_history/<order_number>', views.order_history, name='order_history'),
]
