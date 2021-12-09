from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Articolo, Giornalista


def home(request):
   articoli=Articolo.objects.all()
   giornalisti= Giornalista.objects.all()
   context={"articoli": articoli, "giornalisti": giornalisti}
   print(context)
   return render(requestm, "homepage.html", context)
   