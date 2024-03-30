from django.urls import path
from . import views
urlpatterns =[
    path('',views.tm, name='tm'),
    path('Strona_glowna',views.strona_glowna, name='strona_glowna'),
    path('Zaloguj', views.zaloguj , name='zaloguj'),

]