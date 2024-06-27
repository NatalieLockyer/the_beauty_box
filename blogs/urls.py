from django.urls import path
from . import views
from .views import blogs

urlpatterns = [
    path('', views.blogs, name='blogs'),
]
