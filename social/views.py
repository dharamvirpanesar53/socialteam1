from urllib import request
from django.shortcuts import render, get_object_or_404

from social.models import campaign
from django.views import generic
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):

    camps = campaign.objects.all() 
    
    return render(request, 'index.html', {'camps': camps})

def detail(request, id):
    obj=get_object_or_404(campaign,pk=id)

    return render(request, 'readmore.html', {'obj': obj})

def about(request):
    return render(request, "about.html")
    

    