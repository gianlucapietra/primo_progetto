from django.db import models
from django.db.models.fields import CharField

class Giornalista(models.Model):
    nome=models.CharField(max_length=20)
    cognome=models.CharField(max_length=20)


    def __str__(self):
        return self.nome + " " + self.cognome

class Articolo(models.Model):
    """il modello generico di un articolo di news"""
titolo=models.CharField(max_length=100)#alcuni campi necessitano di parametri obbligatori
contenuto=models.TextField()
giornalista=models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

def __str__(self):
    return self.titolo