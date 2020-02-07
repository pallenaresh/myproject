from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import REG
from .forms import regform, loginform


# Create your views here.
def home(request):
    return render(request,"home.html")
def reg(request):
    if request.method=="POST":
        R = regform(request.POST)
        if R.is_valid():
            S=REG(usermob=R.cleaned_data["usermob1"],Fname=R.cleaned_data["Fname1"],
                Lname=R.cleaned_data["Lname1"],pwd=R.cleaned_data["pwd1"])
            S.save()
            return HttpResponse("reg is successfully")
    else:
        Z=regform()
        return render(request,"reg.html",{"z":Z})
def loginview(request):
    if request.method == "POST":
        S=loginform(request.POST)
        if S.is_valid():
            un=S.cleaned_data["usermob"]
            pw=S.cleaned_data["pwd"]
            D=REG.objects.filter(usermob=un,pwd=pw)
            if not D:
                return HttpResponse("login is failed")
            else:
                return HttpResponse("login is successfully")
    else:
        L=loginform()
        return render(request, "login.html", {"l": L})
def display(request):
    M=REG.objects.all()
    return render(request,"display.html",{"m":M})



