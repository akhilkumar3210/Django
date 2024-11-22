from django.shortcuts import render,redirect
from . forms import *
from . models import *
# Create your views here.

def userform(req):
    if req.method=='POST':
        form1=User(req.POST)
        if form1.is_valid():
            name=form1.cleaned_data['Name']
            age=form1.cleaned_data['Age']
            email=form1.cleaned_data['Email']
            data=Sample.objects.create(Name=name,Age=age,Email=email)
            data.save()
            return redirect(userform)
    form=User()
    return render(req,'user.html',{'form':form})

def mform(req):
    if req.method=='POST':
        form1=Mform(req.POST)
        if form1.is_valid():
            form1.save()
        return redirect(mform)
    form=Mform()
    return render(req,'mform.html',{'form':form})