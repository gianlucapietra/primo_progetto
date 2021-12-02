from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista


def home(request):
    return HttpResponse("<h1>homepage news!</h1>")