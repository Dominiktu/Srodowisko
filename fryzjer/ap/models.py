from django.db import models
from django.core.validators import RegexValidator
class uzytkownicy(models.Model):
    login = models.CharField(max_length=255)
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    nr_tel = models.CharField(
        max_length=9, 
        validators=[
            RegexValidator(
                regex=r'^[0-9\+]+[0-9]{11,17}$|^[0-9]{9,15}$',
                message="wpisz poprawny numer telefony w formacie +48123456789",
                code="Numer telefonu został błednie wprowadzony",
            ),
        ],
    )
    def __str__(Self):
        return self.nr_tel
    haslo = models.CharField(max_length=255) # password = forms.CharField(widget=forms.PasswordInput)
    email = models.CharField(max_length=255, null=True)
    when_to_delete = models.DateField(null=True)
    typ_konta = models.CharField(max_length=255)

class rezerwacje(models.Model):
    id_user =models.IntegerField()
    data = models.DateField(null=True) # tylko dzien 
    timeblocks = models.CharField(max_length=250)
    id_uslugi = models.IntegerField()


class uslugi(models.Model):
    nazwa = models.CharField(max_length=255)
    czas = models.IntegerField()
    


