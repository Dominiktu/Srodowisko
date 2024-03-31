from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import rezerwacje
from datetime import datetime
import calendar

def zarezerwuj(request):
    template = loader.get_template('rezerwacja.html')
    rok = datetime.now().year
    miesiac = datetime.now().month
    wynik = rezerwacje.objects.filter(data__year=rok,data__month=miesiac)
    kalendarz = calendar.monthcalendar(rok, miesiac)


    miesiace = {
        1:"Styczeń",
        2:"Luty",
        3:"Marzec",
        4:"Kwiecień",
        5:"Maj",
        6:"Czerwiec",
        7:"Lipiec",
        8:"Sierpień",
        9:"Wrzesień",
        10:"Październik",
        11:"Listopad",
        12:"Grudzień",
    }
    context = {
        'wynik':wynik,
        'kalendarz':kalendarz,
        'miesiac':miesiace[miesiac],
    }
    return HttpResponse(template.render(context,request))

