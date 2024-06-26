from django.urls import path
from . import views
from .views import collaboration_request

urlpatterns = [
    path('', views.contact, name='contact'),
]
