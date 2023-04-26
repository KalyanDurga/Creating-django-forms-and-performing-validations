from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def student(request):
    SFO=Studentform()
    d={'SFO':SFO}
    if request.method=='POST':
        SD=Studentform(request.POST)
        if SD.is_valid():

            return HttpResponse(str(SD.cleaned_data))
        else:
            return HttpResponse('invalid data')
            

    return render(request,'student.html',d)
