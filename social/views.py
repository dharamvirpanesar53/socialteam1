from django.shortcuts import render

from social.models import campaign

# Create your views here.
def index(request):

    camps = campaign.objects.all() 
    
    return render(request, 'index.html', {'camps': camps})