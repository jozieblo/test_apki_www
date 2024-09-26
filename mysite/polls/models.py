from django.db import models


plec = models.IntegerChoices('Płeć', "Kobieta Mężczyzna Inne")


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nazwa}"

class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=70)
    plec = models.IntegerField(choices=plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(auto_now_add=True, editable=False)
    class Meta:
        ordering= ["nazwisko"]


    def show(self):
        return f"{self.imie} {self.nazwisko}"

    def __str__(self):
        return self.show()



