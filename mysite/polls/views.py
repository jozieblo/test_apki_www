from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
def index(request):
    return HttpResponse("Hello world!.")


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        persons = Osoba.objects.all()
        serializer = OsobaModelSerializer(persons, many=True)
        return Response(serializer.data)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_add(request):
    if request.method == 'POST':
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):
    try:
        person = Osoba.objects.get(id=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        person = Osoba.objects.get(id=pk)
        serializer = OsobaModelSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaModelSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(stanowiska, many=True)
        return Response(serializer.data)
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_add(request):
    if request.method == 'POST':
        serializer = StanowiskoModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(id=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(id=pk)
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoModelSerializer(stanowisko,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)