from django import forms
from .models import uzytkownicy,rezerwacje,uslugi
import re

class uzytkownicy_rejestr(forms.ModelForm):
    haslo=forms.CharField(widget=forms.PasswordInput)
    potwierdz_haslo=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = uzytkownicy
        fields=(
            'imie',
            'nazwisko',
            'nr_tel',
            'login',
            'haslo', 
            'email',
        )
        widgets={
            'nr_tel': forms.TextInput(attrs={
                'placeholder': 'np. +48123456789',
            }),
        }
class uzytkownicy_login(forms.ModelForm):
    class Meta:
        model = uzytkownicy
        fields =(
            'login',
            'haslo'
        )
        widgets ={
            'login': forms.TextInput(attrs={
                'class': "forminput",
            }),
            'haslo': forms.PasswordInput(attrs={
                'class':"forminput",
            })
        }

class uslugi_edit(forms.ModelForm):
    wybory = {"1": "First", "2": "Second"}
    choice_field = forms.ChoiceField(widget=forms.Select, choices=wybory)
    # do sprawdzenia!!!!
    class Meta:
        model = uslugi
        fields=(
            'nazwa',
            'czas',
        )

