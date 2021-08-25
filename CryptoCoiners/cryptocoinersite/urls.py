from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.ulogin, name='ulogin'),
   path('signup/', views.signup, name='signup'),
   path('addcoin/', views.addcoin, name='addcoin'),
]