from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    
    path('register',views.register, name='register'),
     path('login',views.login, name='login'),
     path('logout',views.logout, name='logout'),
     path('upload', views.upload, name='upload'),
     path('post_success', views.post_success, name='post_success'),
     path('profile', views.profile, name='profile'),
     path('option', views.option, name='option'),
     path('business', views.business, name='business'),
     path('post_success2', views.post_success2, name='post_success2'),
     
    


]