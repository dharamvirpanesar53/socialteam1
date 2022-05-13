from unicodedata import name
from django.urls import path
from . import views
from .views import detail


urlpatterns =[
    path('',views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    


]