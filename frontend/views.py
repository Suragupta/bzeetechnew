from django.shortcuts import render
from backend.models import *

# Create your views here.
def home(request):
     topbar_data=topbar_DB.objects.filter(status=True)
     card_data=service_card_DB.objects.filter(status=True)
     return render(request, "index.html", {"topbar_data":topbar_data,"card_data":card_data})
    
   
def about(request):
    return render(request, 'about.html', {})


        
        
        
        
        
        
        
    
    
    
    