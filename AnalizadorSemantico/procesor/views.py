from motor.reader import initScan

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
# crear una interfaz grafica para subir archivo.txt para ser analizado.


def home(request):
    return render(request, 'home.html')


def runCheck(request):
    result = initScan()
    return JsonResponse(result)
