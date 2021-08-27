from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   
   path('dashboard/', views.dashboard, name='dashboard'),
   path('allcoin/', views.allcoin, name='allcoin'),
   path('users/', views.users, name='users'),
   path('newcoin/', views.newcoin, name='newcoin'),
   path('adds/', views.adds, name='adds'),
   path('status/<int:id>', views.status,name='status'),
   path('delete/<int:id>', views.delete,name='delete'),
   path('update/<int:id>', views.update,name='update'),
  
]