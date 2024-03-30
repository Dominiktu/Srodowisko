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

def zaloguj(reqest):
    template = loader.get_template('logowanie.html')
    context ={

    }
    form = uzytkownicy_rejestr(request.POST or None)
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
        
        
# TO DO: REWORK 
# def Strona_Umawiania_wizyt(request):
#     template = loader.get_template('kalendarz.html')
#     return HttpResponse(template.render(request))

# def Strona_Terminarza(request):
#     template = loader.get_template('kalendarz.html')
#     return HttpResponse(template.render(request))

 
# def Logowanie_Dla_Fryzjer_Ap_forms(request):
#     template = loader.get_template("logowanie.html")

#     form = uzytkownicy_login(request.POST or None)
#     if form.is_valid():
#         form.save()
#         context = {
#             'form' : form
#         }

#     return HttpResponse(template.render(request))
# def form_rejestr(request):
#     template = loader.get_template('Rejestracja.html')

#     form = uzytkownicy_rejestr(request.POST or None)
#     if form.is_valid():
#         form.save()
#         context = {
#             'form' : form
#         }


    
    

