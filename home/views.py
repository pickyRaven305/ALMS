from django.shortcuts import render
from .models import Contact
# Create your views here.
#loading home page
def index(request):
    return render(request, 'home/index.html')

#loading services page

def services(request):
    return render(request, 'home/services.html')

#loading about page

def about(request):
    return render(request, 'home/about.html')

#loading connections page

def connections(request):
    return render(request, 'home/connections.html')

#loading contact page

def contact(request):
    if request.method=='POST':
        # getting details form html page
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Phone")
        message = request.POST.get("Message")
        
        contact = Contact(name=name,email=email,number=phone,message=message)
        contact.save()      
        
    return render(request, 'home/contact.html')