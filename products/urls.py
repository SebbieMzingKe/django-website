from django.urls import path
from . import views
urlpatterns = [
    path('',views.index), 
    path('new', views.new),
    path('search/',views.search_fruits, name = 'search_fruits'),
]
