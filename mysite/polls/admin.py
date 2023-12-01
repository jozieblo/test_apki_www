from django.contrib import admin
from .models import  Osoba, Stanowisko



class OsobaAdmin(admin.ModelAdmin):
    list_display = ('id','imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania')
    list_filter = ('stanowisko', 'data_dodania')

    @admin.display(description='Stanowisko')
    def stanowisko(self, obj):
        if obj.stanowisko:
            return f"{obj.stanowisko} ({obj.stanowisko.id})"
        else:
            return None

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)
