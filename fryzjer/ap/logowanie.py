from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import re
from django.db import models
from .models import uzytkownicy
from .forms import uzytkownicy_login,uzytkownicy_rejestr

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
    form = uzytkownicy_rejestr(request.POST or None)
    error=""
    regex="[0-9\+]+[0-9]{11,17}$|^[0-9]{9,15}$"
    if form.is_valid():
        if (request.POST.get("haslo","") == request.POST.get("potwierdz_haslo","")) and (re.match(regex,request.POST.get("nr_tel","")) != None) and (uzytkownicy.objects.filter(login=request.POST.get("login","")).count() == 0):
            rekord = uzytkownicy.objects.create(
                login=request.POST.get("login",""),
                imie=request.POST.get("imie",""),
                nazwisko=request.POST.get("nazwisko",""),
                nr_tel=request.POST.get("nr_tel",""),
                haslo=request.POST.get("haslo",""),
                email=request.POST.get("email",""),
                typ_konta="klient"
            )
            rekord.save()
            request.session['id']=uzytkownicy.objects.filter(login=request.POST.get("login",""),haslo=request.POST.get("haslo",""))[0].id
            return redirect("strona_glowna")
        elif (request.POST.get("haslo","") != request.POST.get("potwierdz_haslo","")):
            error="wpisanie hasla nie zgadzają sie"
        elif uzytkownicy.objects.filter(login=request.POST.get("login","")).count() > 0:
            error="podany login jest już zajęty"
    elif (request.POST.get("haslo","") != request.POST.get("potwierdz_haslo","")):
        error="wpisanie hasla nie zgadzają sie"
    elif re.match(regex,request.POST.get("nr_tel","")) == None:
        error="wpisz poprawny numer telefonu w formacie +48123456789"
        if request.POST.get("nr_tel","") == "":
            error=""
    elif uzytkownicy.objects.filter(login=request.POST.get("login","")).count() > 0:
        error="podany login jest już zajęty"
    context ={
        'form':form,
        'error':error
    }  
    return HttpResponse(template.render(context,request))
