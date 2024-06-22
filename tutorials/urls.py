from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tutorials, name='tutorials'),
    path('<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
]
