from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.db import models
from .forms import uzytkownicy_login
from .forms import uzytkownicy_rejestr
def strona_glowna(request): # <-- to strona główna
    template = loader.get_template('strona_glowna.html')
    context={
        
    }
    return HttpResponse(template.render(context,request))
def tm(request):
    return redirect("strona_glowna")

def wyloguj(reqest):
    reqest.session.flush()
    return redirect("strona_glowna")
    

