from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Index', views.Index, name='Index'),
    path('Home', views.Home, name="Home"),
    path('IfTagDemo', views.igtagdemo, name='IfTagDemo'),
    path('ShowProducts', views.ShowProducts, name='ShowProducts'),
    path('ShowUsers', views.LoadUsers, name='LoadUsers'),
    path('ShowUsers2', views.LoadUsers2, name='LoadUsers2'),
    path('ShowUsersDetails', views.LoadUserDetails, name='ShowUsersDetails'),
    path('PassModel', views.PassModelToTemplate, name='PassModel'),
    path('BIFDemo', views.BuiltInFiltersDemo, name='BIFDemo'),
    path('TestStaticFiles', views.TestStaticFiles, name="TestStaticFiles")
]