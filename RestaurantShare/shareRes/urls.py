from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreate/', views.restaurantCreate),
    path('categoryCreate/',views.categoryCreate),
]