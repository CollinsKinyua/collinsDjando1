from django.shortcuts import render
from djangoFoxx.form import Empform


def Home(request):
    return render(request, 'Index.html')


def About(request):
    return render(request, 'About us.html')


def contact(request):
    return render(request, 'contactus.html')

def myform(request):
    stu=Empform()
    return render(request, 'forms.html', {'form':stu})



