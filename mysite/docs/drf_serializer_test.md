from ankiety.models import Osoba
from ankiety.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

osoba = Osoba(imie='Kamil', nazwisko='Nowak')
person.save()

serializer = OsobaSerializer(osoba)
serializer.data

content = JSONRenderer().render(serializer.data)
content

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PersonSerializer(data=data)
deserializer.is_valid()

deserializer.errors

repr(deserializer)
deserializer.validated_data
deserializer.save()
deserializer.data