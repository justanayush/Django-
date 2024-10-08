from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.dc_sup, name='all_sup'),
    
    path('<int:sup_id>/', views.sup_detail, name='sup_detail')


]
