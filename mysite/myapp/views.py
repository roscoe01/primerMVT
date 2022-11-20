from django.shortcuts import render

# Create your views here.

# Una vista es una funcion 

from django.http import HttpResponse

from .models import Persona

def index(request):
    return HttpResponse("Kiss me")


def persona_por_id(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    return HttpResponse(f"Persona: {persona.apellido}, {persona.nombre}")
