from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.db import models
from .models import uzytkownicy
from .forms import uzytkownicy_login

def zaloguj(request):
    template = loader.get_template('logowanie.html')
    context ={

    }
    form = uzytkownicy_login(request.POST or None)
    if form.is_valid():
        # check if user is in DATE BASE
        if(jest_w_DB):
            reqest.session['zologany_imie']
            reqest.session['zologany_ID']
            reqest.session['cos']
        else:
            # ODDAJ ERROR
            pass
    context ={
        'form':form,
    }  
    return HttpResponse(template.render(context,request))
