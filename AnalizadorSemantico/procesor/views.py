from django.shortcuts import render, HttpResponse

# Create your views here.

# crear una interfaz grafica para subir archivo.txt para ser analizado.


def home(request):
    return HttpResponse("home Page")
