from django.urls import path

from . import views

urlpatterns = [
    #change to the get_data view
    path('',views.getKeyspaces, name="getKeyspaces"),
    path('<int:emp_id>/', views.details, name='details'),
    path('display/', views.displayTables, name='displayTables'),
    path('display/insert', views.newQuery, name='newQuery'),
    path('display/', views.tableDetails, name='tableDetails'),

]