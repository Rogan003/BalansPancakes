from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Prodaja
from django.contrib import messages
# Create your views here.
def home(request):
    prodaje = Prodaja.objects.all()
    y=0
    for x in prodaje:
        if x.godina==2021:
            y+=1
    if y==0:
        Prodaja.objects.create(godina = 2021, brojPalacinaka = 181783)
    else:
        messages.info(request,"Ova godina je vec uneta!")
    prodaje = Prodaja.objects.all()
    return render(request,'balanspalacinke.html',{'prodaja' : prodaje})