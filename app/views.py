from django.shortcuts import render
from .models import Entry
# Create your views here.

def index(request):
    
    return render(request,"index.html")


def about_us(request):
    
    return render(request,"about_us.html")


def project(request):
    
    return render(request, 'myproject.html')



def contact(request):
    if request.method == "POST":
        print(123)
        username = request.POST.get("name")
        useremail = request.POST.get('email')
        textfield = request.POST.get('text')  
        storedata = Entry(username=username,useremail=useremail,textfield = textfield)
        storedata.save()
    return render(request, 'contact.html')