# Generated by Django 5.0.2 on 2024-03-01 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ap', '0002_delete_rezerwacje_delete_uslugi_delete_uzytkownicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='rezerwacje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('data', models.DateField(null=True)),
                ('timeblocks', models.CharField(max_length=250)),
                ('id_uslugi', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='uslugi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255)),
                ('czas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='uzytkownicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('imie', models.CharField(max_length=255)),
                ('nazwisko', models.CharField(max_length=255)),
                ('nr_tel', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='Numer telefonu został błednie wprowadzony', message='wpisz poprawny numer telefony w formacie +48123456789', regex='^[0-9\\+]+[0-9]{11,17}$|^[0-9]{9,15}$')])),
                ('haslo', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('when_to_delete', models.DateField(null=True)),
                ('typ_konta', models.CharField(max_length=255)),
            ],
        ),
    ]
