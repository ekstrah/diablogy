from django.urls import path

from . import views

urlpatterns = [
    #change to the get_data view
    path('',views.DisplayRows, name="DisplayRows"),
    path('newQuery/',views.newQuery, name="newQuery"),
    path('<int:emp_id>/', views.details, name='details'),

]