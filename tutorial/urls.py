from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_tutorials, name='tutorial'),
    path('<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('add/', views.add_tutorial, name='add_tutorial'),
    path('edit/<int:tutorial_id>/', views.edit_tutorial, name='edit_tutorial'),
    path('delete/<int:tutorial_id>/', views.delete_tutorial, name='delete_tutorial'),
]
