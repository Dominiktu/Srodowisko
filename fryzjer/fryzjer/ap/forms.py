from django import forms
from .models import uzytkownicy,rezerwacje,uslugi

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
        )
    def clean(self):
        dane = super(uzytkownicy_rejestr, self).clean()
        haslo = dane.get('haslo')
        potwierdz_haslo = dane.get('potwierdz_haslo')
        if haslo != potwierdz_haslo:
            raise forms.ValidationError(
                "hasła nie są takie same"
            )
 
class uzytkownicy_login(forms.ModelForm):
    haslo=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = uzytkownicy
        fields =(
            'login',
            'haslo'
        )

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
