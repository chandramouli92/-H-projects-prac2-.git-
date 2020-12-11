from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('base',views.base,name="base"),
    path('name',views.name,name="name"),
    path('wel',views.wel,name="wel"),
    path('mouli',views.mouli,name="name"),
]
