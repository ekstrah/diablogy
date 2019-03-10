from django.urls import path

from . import views

urlpatterns = [
    #change to the get_data view
    path('', views.index, name='index'),
]