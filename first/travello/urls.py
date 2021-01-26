from django.urls import path
from . import views
from .views import dests

urlpatterns = [
    path('', views.index, name = 'index')
]
for dest in views.dests:
    urlpatterns = urlpatterns + [path('destinations/'+dest.name, views.destination, name = 'destinations'+dest.name)]