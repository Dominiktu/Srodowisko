from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.db import models
from .models import uzytkownicy
from .forms import uzytkownicy_login

def zaloguj(request):
    if  request.session.get('id','') != "":
        return redirect("strona_glowna")
    template = loader.get_template('logowanie.html')
    context ={

    }
    form = uzytkownicy_login(request.POST or None)
    error=0
    if form.is_valid():
        wynik=uzytkownicy.objects.filter(login=request.POST.get("login",""),haslo=request.POST.get("haslo",""))
        if wynik.count() == 1:
            request.session['id']=wynik[0].id
            return redirect("strona_glowna")
        else:
            error="1"
    context ={
        'form':form,
        'error':error
    }  
    return HttpResponse(template.render(context,request))

def rejestr(request):
    template = loader.get_template('rejestr.html')
    context ={

    }
    form = uzytkownicy_login(request.POST or None)
    error=0
    if form.is_valid():
        wynik=uzytkownicy.objects.filter(login=request.POST.get("login",""),haslo=request.POST.get("haslo",""))
        if wynik.count() == 1:
            request.session['id']=wynik[0].id
            return redirect("strona_glowna")
        else:
            error="1"
    context ={
        'form':form,
        'error':error
    }  
    return HttpResponse(template.render(context,request))
