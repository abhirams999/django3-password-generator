from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    length=int(request.GET.get('length'))
    lst=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        lst.extend(list('ABCDEFGHIJKLMNOPQRSTUWXYZ'))
    if request.GET.get('numbers'):
        lst.extend(list('123456789'))
    if request.GET.get('special'):
        lst.extend(list('@#$%*&'))
    thepassword=''
    for i in range(length):
        thepassword+=choice(lst)

    return render(request,'generator/password.html',{'password':thepassword})
def about(request):
    return render(request,'generator/about.html')
