"""ALMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
app_name = "donation"

urlpatterns = [

    path('<int:pk>/add_item/', views.add_item, name='add_item'),
    path('<int:pk>/order_item/', views.order_item, name='order_item'),
    path('<int:pk>/uploads/', views.uploads, name='uploads'),
    path('<int:pk>/order_history/', views.order_history, name='order_history'),
    path('<int:pk>/donation_history/', views.donation_history, name='donation_history'),
    path('<int:pk>/donate/', views.donate, name='donate'),
    path('Payments/', views.Payments, name='Payments'),
    

] 
