from django.urls import path
from places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.places_list, name='places_list'),
    path('places/<int:pk>/', views.place_detail, name='place_detail'),
    path('places/add/', views.add_place, name='add_place'),
]
