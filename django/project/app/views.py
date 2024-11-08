from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

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
def fun3(req):
        a=['name','place','address']
        b='name','place','address'
        c=[9,1,4,2,3,5,6,8]
        d=[{'name':'Athul','place':'Ernakulam','age':21},{'name':'Nabeel','place':'palakad','age':20},{'name':'Vishnu','place':'Thrissur','age':23}]
        return render(req,'demo.html',{'data':a,'b':b,'c':c,'d':d})
def fun4(req):
    a=[{'name':'Athul','place':'Ernakulam','age':21},{'name':'Nabeel','place':'palakad','age':20},{'name':'Vishnu','place':'Thrissur','age':23},{'name':'Anand','place':'kozhikode','age':45},{'name':'Sreehari','place':'Wayand','age':33},{'name':'Deepu','place':'Kottayam','age':29},{'name':'Neeraj','place':'Idukki','age':22},{'name':'Dhijin','place':'Polachi','age':30},{'name':'Shaheen','place':'Munnar','age':25},{'name':'Vivek','place':'Walayar','age':34},{'name':'Hakkem','place':'Banglore','age':19},{'name':'Apputten','place':'palani','age':31},{'name':'Abhinav','place':'Kannur','age':38},{'name':'Shaneeb','place':'kollam','age':25},{'name':'Shaheer','place':'Chennai','age':40}]
    
    l1=[]
    l2=[]
    for i in a:
        if i['age']>=30:
            l1.append(i)
        else:
            l2.append(i)
    return render(req,'table.html',{'a':a,'l1':l1,'l2':l2})

std=[]

def addstd(req):
    if req.method=='POST':
        r=req.POST['roll_no']
        n=req.POST['name']
        a=req.POST['age']
        data=Student.objects.create(roll_no=r,name=n,age=a)
        data.save()
        # std.append({'roll_no':r,'name':n,'age':a})
        # print(std)
        return redirect(addstd)
    else:
        data=Student.objects.all()
        return render(req,'adstd.html',{'std':data})
    
def editstd(req,id):
    # student=''
    # for i in std:
    #     if i['roll_no']==id:
    #         student=i
            # print(student)
    data=Student.objects.get(pk=id)
    if req.method=='POST':
        r=req.POST['roll_no']
        n=req.POST['name']
        a=req.POST['age']
        # student['roll_no']=r
        # student['name']=n
        # student['age']=a
        data=Student.objects.filter(pk=id).update(roll_no=r,name=n,age=a)
        return redirect(addstd)
    else:
        return render(req,'edit.html',{'data':data})
    
def delstd(req,id):
    # for i in std:
    #     if i['roll_no']==id:
    #         std.remove(i)
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(addstd)