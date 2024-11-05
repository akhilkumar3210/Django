from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("Hello World")
def fun2(request,a,b):
    return HttpResponse(a)
def bonus(req,s,y):
    if y>5:
        b=s*5/100
        return HttpResponse (b)
    else:
        return HttpResponse(s)
def digits(req,a):
    b=a%10
    if b%3==0:
        return HttpResponse('divisible')
    else:
        return HttpResponse('Not divisible')
def bills(req,u):
    if u<100:
        return HttpResponse("No Charge")
    elif u<200:
        a=(u-100)*5
        return HttpResponse(a)
    else:
        a=(100*5)+(u-200)*10
        return HttpResponse(a)
def city(req,c):
    if c=='delhi':
        return HttpResponse("Red Fort")
    elif c=='agra':
        return HttpResponse("Taj Mahal")
    elif c=='jaipur':
        return HttpResponse("Jal Mahal")
    else:
        return HttpResponse("no monument in cities")
def days(req,d):
    if d==1:
        return HttpResponse("Sunday")
    elif d==2:
        return HttpResponse("Monday")
    elif d==3:
        return HttpResponse("Tuesday")
    elif d==4:
        return HttpResponse("Wensday")
    elif d==5:
        return HttpResponse("Thursday")
    elif d==6:
        return HttpResponse("Friday")
    elif d==7:
        return HttpResponse("Saturday")
    else:
        return HttpResponse("invaild ")
def tax(req,pb):
    if pb<=50000:
        tax=pb*5/100
        return HttpResponse(tax)
    elif pb>50000 and pb<=100000:
        tax=pb*10/100
        return HttpResponse(tax)
    elif pb>100000:
        tax=pb*15/100
        return HttpResponse(tax)
    else:
        return HttpResponse('no ')