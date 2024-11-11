from django.shortcuts import render

# Create your views here.
def book(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def service(req):
    return render(req,'services.html')
def price(req):
    return render(req,'pricing.html')
def car(req):
    return render(req,'car.html')
