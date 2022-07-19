
from django.urls import path

from . import views

app_name = "car"

urlpatterns =  [

path('detail/<str:pk>/',views.Detail.as_view(),name="detail"),
path('list',views.List.as_view(),name="list"),
path('create',views.Create,name="create"),
 
]