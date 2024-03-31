from django.urls import path
from . import views,logowanie
urlpatterns =[
    path('',views.tm, name='tm'),
    path('Strona_glowna',views.strona_glowna, name='strona_glowna'),
    path('wyloguj', views.wyloguj , name='wyloguj'),
    path('Zaloguj', logowanie.zaloguj , name='zaloguj'),
]