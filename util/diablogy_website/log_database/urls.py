from django.urls import path

from . import views

urlpatterns = [
    #change to the get_data view
    path('',views.DisplayRows, name="DisplayRows"),
    path('<int:emp_id>/', views.details, name='details')
]