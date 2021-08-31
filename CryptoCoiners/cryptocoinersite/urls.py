from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.ulogin, name='ulogin'),
   path('signup/', views.signup, name='signup'),
   path('addcoin/', views.addcoin, name='addcoin'),
   path('logout/', views.ulogout, name='ulogout'),
   path('disclaimer/', views.disclaimer, name='disclaimer'),
   path('privacy/', views.privacy, name='privacy'),
   path('terms/', views.terms, name='terms'),
   path('promote/', views.promote, name='promote'),
   path('coin/<int:id>', views.coin, name='coin'),
   path('myvote/', views.myvote, name='myvote'),
   path('new/', views.new, name='new'),
   path('all/', views.all, name='all'),
   path('presale/', views.presale, name='presale'),
   path('upload/', views.upload, name='upload'),
   
]