from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba
from .serializers import OsobaSerializer
def index(request):
    return HttpResponse("Hello world!.")


@api_view(['GET'])
def person_list(request):
    if request.method == 'GET':
        persons = Osoba.objects.all()
        serializer = OsobaSerializer(persons, many=True)
        return Response(serializer.data)