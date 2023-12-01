from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


plec = models.IntegerChoices('Płeć', "Kobieta Mężczyzna Inne")

def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError('Nazwa może zawierać tylko litery.')

def validate_past_date(value):
    current_date = timezone.now().date()
    if value > current_date:
        raise ValidationError('Data dodania nie może być z przyszłości.')
class Stanowisko(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nazwa}"

class Osoba(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50, validators=[validate_alpha])
    nazwisko = models.CharField(max_length=70, validators=[validate_alpha])
    plec = models.IntegerField(choices=plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(default=timezone.now, validators=[validate_past_date])
    class Meta:
        ordering= ["nazwisko"]


    def show(self):
        return f"{self.imie} {self.nazwisko}"

    def __str__(self):
        return self.show()



