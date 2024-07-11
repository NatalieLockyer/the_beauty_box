from django.urls import path

from . import views
from .views import contact

urlpatterns = [
    path('', views.contact, name='contact'),
]
