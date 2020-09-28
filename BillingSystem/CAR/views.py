from django.shortcuts import render
from django.views.generic.list import ListView
from .models import customer,car

# Create your views here.
def home(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def report(request):
    return render(request,'base_report.html')

# def listing(request):
#    return render(request,'base_listing.html')

def dashbord(request):
    return render(request,'base_dashbord.html')

def login(request):
    return render(request,'login.html')



class customerView(ListView):
    model = customer
    template_name ='base_listing.html'