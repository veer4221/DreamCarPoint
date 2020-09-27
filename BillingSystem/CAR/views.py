from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def report(request):
    return render(request,'base_report.html')

def listing(request):
    return render(request,'base_listing.html')

def dashbord(request):
    return render(request,'base_dashbord.html')

def login(request):
    return render(request,'login.html')

