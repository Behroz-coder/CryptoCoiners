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
   path('promoted/', views.promoted, name='promoted'),
   path('today/', views.today, name='today'),
   path('newcoins/', views.newcoins, name='newcoins'),
   path('alltimebest/', views.alltimebest, name='alltimebest'),
   path('presal/', views.presal, name='presal'),
   path('status/<int:id>', views.status,name='status'),
   path('delete/<int:id>', views.delete,name='delete'),
   path('udelete/<int:id>', views.udelete,name='udelete'),
   path('update/<int:id>', views.update,name='update'),
   path('deleteimage/<int:id>', views.deleteimage, name='deleteimage'),
   
]